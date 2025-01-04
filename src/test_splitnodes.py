import unittest

from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.NORMAL),
            ],
            new_nodes,
        )
    
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )
    
    def test_other_text_to_texnodes(self):
        nodes = text_to_textnodes("**Brand new text** mixing *styles* and `combining other elements` like this ![duck image](https://i.imgur.com/0KQGK8l.jpeg)")
        
        self.assertEqual(
            [
                TextNode("Brand new text", TextType.BOLD),
                TextNode(" mixing ", TextType.NORMAL),
                TextNode("styles",TextType.ITALIC),
                TextNode(" and ", TextType.NORMAL),
                TextNode("combining other elements", TextType.CODE),
                TextNode(" like this ", TextType.NORMAL),
                TextNode("duck image", TextType.IMAGE,"https://i.imgur.com/0KQGK8l.jpeg"),
            ],
            nodes,
        )
        pass