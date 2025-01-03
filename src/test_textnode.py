import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not the same text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_eq_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_eq_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
    
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_eq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

#Test TextNode conversion
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_html_node_bold(self):
        node = TextNode("This is a bold move", TextType.BOLD )
        html_node = text_node_to_html_node(node)
        assert html_node.to_html() == "<b>This is a bold move</b>"
    
    def test_text_node_html_node_link(self):
        node = TextNode("Click Here", TextType.LINK, "https://www.google.com" )
        html_node = text_node_to_html_node(node)
        assert html_node.to_html() == '<a href="https://www.google.com">Click Here</a>'

    def test_text_node_html_node_raw(self):
        node = TextNode("Is this a raw test?", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        assert html_node.to_html() == "Is this a raw test?"
    
    """
    def test_text_node_html_node_invalid_type(self):
        try:
            node = TextNode("This is not supported", TextType.UNDERLINE)        
            html_node = text_node_to_html_node(node)
            assert html_node.to_html() == "Unknown TextType"
        except ValueError as  e:
            assert str(e) == "Unknown TextType"
        """

if __name__ == "__main__":
    unittest.main()