import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_url_none(self):
        node = TextNode("text", TextType.LINK, url = None )
        node2 = TextNode("text", TextType.LINK, url = None )
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.IMAGE, url="http://example.com/image.png")
        node_repr = TextNode("This is a text node", TextType.CODE, url="http://example.com/image.png")
        self.assertNotEqual(node, node_repr)



if __name__ == "__main__":
    unittest.main()
