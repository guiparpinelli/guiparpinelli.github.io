"""Text-level checks for the static landing page. Python stdlib only."""

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

FORBIDDEN = ("omarchy", "depoimento", "preço", "clientes", "métrica", "download")


class Node:
    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []

    def text(self):
        parts = []
        for child in self.children:
            if isinstance(child, str):
                parts.append(child)
            else:
                parts.append(child.text())
        return re.sub(r"\s+", " ", "".join(parts)).strip()


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def walk(node):
    for child in node.children:
        if isinstance(child, Node):
            yield child
            yield from walk(child)


def element_children(node):
    return [child for child in node.children if isinstance(child, Node)]


def load():
    html = INDEX.read_text(encoding="utf-8")
    parser = Tree()
    parser.feed(html)
    return html, parser.root


def style_text(html):
    chunks = re.findall(r"<style\b[^>]*>(.*?)</style>", html, flags=re.I | re.S)
    for tag in re.findall(r"<link\b[^>]*>", html, flags=re.I):
        if not re.search(r"rel\s*=\s*[\"']stylesheet[\"']", tag, flags=re.I):
            continue
        match = re.search(r"href\s*=\s*[\"']([^\"']+)[\"']", tag, flags=re.I)
        if not match:
            continue
        href = match.group(1)
        if href.startswith(("http://", "https://", "//")):
            chunks.append(href)
            continue
        path = (ROOT / href.lstrip("/")).resolve()
        if path.is_file():
            chunks.append(path.read_text(encoding="utf-8"))
    chunks.extend(re.findall(r"\bstyle\s*=\s*[\"']([^\"']*)[\"']", html, flags=re.I))
    return "\n".join(chunks)


class LandingPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html, cls.root = load()
        cls.css = style_text(cls.html)

    def test_html_lang_pt(self):
        self.assertIn("<html lang=\"pt\">", self.html)
        html_el = next(el for el in walk(self.root) if el.tag == "html")
        self.assertEqual(html_el.attrs.get("lang"), "pt")

    def test_single_h1_parpi(self):
        headings = [el for el in walk(self.root) if el.tag == "h1"]
        self.assertEqual(len(headings), 1, [h.text() for h in headings])
        self.assertEqual(headings[0].text(), "parpi")

    def test_name_appears(self):
        self.assertIn("Guilherme Parpinelli", self.html)

    def test_one_github_claim_link(self):
        matches = []
        for el in walk(self.root):
            if el.tag != "a":
                continue
            if el.attrs.get("href") != "https://github.com/guiparpinelli":
                continue
            if el.text() == "Abrir o GitHub":
                matches.append(el)
        self.assertEqual(len(matches), 1)

    def test_nav_section_links(self):
        navs = [el for el in walk(self.root) if el.tag == "nav"]
        self.assertGreaterEqual(len(navs), 1)
        hrefs = set()
        for nav in navs:
            for el in walk(nav):
                if el.tag == "a" and "href" in el.attrs:
                    hrefs.add(el.attrs["href"])
        self.assertTrue({"#pagina", "#fora", "#fecho"} <= hrefs)

    def test_section_ids(self):
        ids = {el.attrs.get("id") for el in walk(self.root)}
        self.assertTrue({"pagina", "fora", "fecho"} <= ids)

    def test_blank_produto_and_correio(self):
        pairs = set()
        for el in walk(self.root):
            kids = element_children(el)
            for left, right in zip(kids, kids[1:]):
                pairs.add((left.text(), right.text()))
        self.assertIn(("Produto", "em branco"), pairs)
        self.assertIn(("Correio", "em branco"), pairs)

    def test_stylesheet_has_no_motion(self):
        css = self.css.lower()
        self.assertNotIn("@keyframes", css)
        self.assertNotIn("animation:", css)
        self.assertNotIn("transition:", css)

    def test_forbidden_substrings(self):
        haystack = self.html.lower()
        for word in FORBIDDEN:
            self.assertNotIn(word, haystack)

    def test_fonts_are_local_font_face_only(self):
        lowered = self.html.lower()
        self.assertNotIn("fonts.googleapis.com", lowered)
        self.assertNotIn("jsdelivr", lowered)
        self.assertIn("@font-face", self.css.lower())
        urls = re.findall(r"url\(\s*[\"']?([^\"')]+)", self.css, flags=re.I)
        self.assertGreaterEqual(len(urls), 1)
        for url in urls:
            self.assertFalse(url.lower().startswith(("http://", "https://", "//")))
            self.assertNotIn("fonts.googleapis.com", url.lower())
            self.assertNotIn("jsdelivr", url.lower())
            self.assertTrue(
                url.startswith(("fonts/", "./fonts/", "/fonts/")),
                url,
            )


if __name__ == "__main__":
    unittest.main()
