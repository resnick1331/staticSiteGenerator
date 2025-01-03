import unittest

from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_code(self):
        """Tests splitting nodes for code blocks."""
        old_nodes = [TextNode("This is text with a `code block` word", TextType.NORMAL)]
        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, "`", TextType.CODE), expected_nodes)
    
    def test_split_nodes_bold(self):
        """Tests splitting nodes for bold text."""
        old_nodes = [TextNode("This is **bold** text", TextType.NORMAL)]
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, "**", TextType.BOLD), expected_nodes)

    def test_split_nodes_italic(self):
        """Tests splitting nodes for italic text."""
        old_nodes = [TextNode("This is *italic* text", TextType.NORMAL)]
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, "*", TextType.ITALIC), expected_nodes)