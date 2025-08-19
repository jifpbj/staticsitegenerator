import unittest

from markdown_blocks import block_to_block_type, BlockType

class TestHTMLNode(unittest.TestCase):
    def test_heading_eq(self):
        heading = "### This is the Title"
        test = block_to_block_type(heading)
        answer = BlockType.HEADING
        self.assertEqual(test, answer)
        
    def test_heading_eq2(self):
        heading = "This is ### the Title"
        test = block_to_block_type(heading)
        answer = BlockType.HEADING
        self.assertNotEqual(test, answer)

    def test_code_eq(self):
        code = "```python\nprint('Hello, World!')\n```"
        test = block_to_block_type(code)
        answer = BlockType.CODE
        self.assertEqual(test, answer)

    def test_quote_eq(self):
        quote = "> This is a quote"
        test = block_to_block_type(quote)
        answer = BlockType.QUOTE

    def test_quote_multiline_eq(self):
        quote = "> This is a quote \n> with multiple lines"
        test = block_to_block_type(quote)
        answer = BlockType.QUOTE
        self.assertEqual(test, answer)
        
    def test_unordered_list_eq(self):
        unordered_list = "- Item 1\n- Item 2\n- Item 3"
        test = block_to_block_type(unordered_list)
        answer = BlockType.UNORDERED_LIST
        self.assertEqual(test, answer)

    def test_unordered_list_noteq(self):
        unordered_list = "- Item 1\n# Item 2\n- Item 3"
        test = block_to_block_type(unordered_list)
        answer = BlockType.UNORDERED_LIST
        self.assertNotEqual(test, answer)

    def test_ordered_list_eq(self):
        ordered_list = "1. Item 1\n2. Item 2\n3. Item 3"
        test = block_to_block_type(ordered_list)
        answer = BlockType.ORDERED_LIST
        self.assertEqual(test, answer)

    def test_ordered_list_uneq(self):
        ordered_list = "1. Item 1\n4. Item 2\n5. Item 3"
        test = block_to_block_type(ordered_list)
        answer = BlockType.ORDERED_LIST
        self.assertNotEqual(test, answer)

