import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        check = f' href="google.com" target="_blank"'
        self.assertEqual(output, check)

class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        from htmlnode import LeafNode
        node = LeafNode("p", "Hello, World!", {"class": "text"})
    def test_leaf_node_to_html(self):
        node = LeafNode("p", "Hello, World!", {"class": "text"})
        self.assertEqual(node.to_html(), '<p class="text">Hello, World!</p>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
