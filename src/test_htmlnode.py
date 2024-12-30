import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    #Tests for LeafNode
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
    
    #Tests for ParentNodes
    def test_parent_node_to_html_no_tag(self):
        node = ParentNode(None, [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],None )
        try:
            assert node.to_html() == "ParentNode must have a tag"
        except ValueError as e:
            assert str(e) == "ParentNode must have a tag"

    def test_parent_node_to_html_no_children(self):
        node = ParentNode("div", None)
        try:
            assert node.to_html() == "ParentNode must have children"
        except ValueError as e:
            assert str(e) == "ParentNode must have children"

    def test_parent_node_simple(self):
        node = ParentNode(
            "ul",
            [
                LeafNode("li", "Item 1"),
                LeafNode("li", "Item 2"),
            ],
        )
        assert node.to_html() == "<ul><li>Item 1</li><li>Item 2</li></ul>"
    
    def test_parent_node_nested(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "Paragraph 1"),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                    ],
                ),
                LeafNode("p", "Paragraph 2"),
            ],
        )
        assert node.to_html() == "<div><p>Paragraph 1</p><ul><li>Item 1</li><li>Item 2</li></ul><p>Paragraph 2</p></div>"

    def test_parent_node_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Content")],
            props={"class": "container"},
        )
        assert node.to_html() == '<div class="container"><p>Content</p></div>'