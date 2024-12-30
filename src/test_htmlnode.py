import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        assert node.props_to_html() == ""

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        assert node.props_to_html() == ' href="https://www.google.com"'


    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        assert node.props_to_html() == ' href="https://www.google.com" target="_blank"'
    
    def test_leaf_node_props_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        assert node.props_to_html() == ' href="https://www.google.com"'
    
    def test_leaf_node_to_html_no_tag(self):
        node = LeafNode(None, "This sample text doesnt have tags")
        assert node.to_html() == "This sample text doesnt have tags"
    
    def test_leaf_node_to_html_tag(self):
        node = LeafNode("b", "This is the last sentence")
        assert node.to_html() == "<b>This is the last sentence</b>"
    
    def test_leaf_node_no_value(self):
        node = LeafNode("p")
        try:
            assert node.to_html() == "LeafNode must have a value"
        except ValueError as e:
            assert str(e) == "LeafNode must have a value"
