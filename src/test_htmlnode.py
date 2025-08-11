import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_not_eq(self):
        node = HTMLNode("p", "Hello, World!", [], {"class": "text"})
        node2 = HTMLNode("div", "container", [node], {"class": "container"})
        self.assertNotEqual(node, node2)
    def test_eq(self):
        node = HTMLNode("p", "Hello, World!", [], {"class": "text"})
        node2 = HTMLNode("p", "Hello, World!", [], {"class": "text"})
        self.assertNotEqual(node, node2)
    def test_url_none(self):
        node = HTMLNode("p", "Sure", [], {"href": "google.com", "target": "_blank"})
        output = node.props_to_html()
        check = f'href="google.com" target="_blank"'
        self.assertEqual(output, check)
if __name__ == "__main__":
    unittest.main()
