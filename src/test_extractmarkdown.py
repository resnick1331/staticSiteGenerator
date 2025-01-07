import re
from unittest import TestCase

from extractmarkdown import (
    extract_markdown_images, 
    extract_markdown_links, 
    extract_title, 
    markdown_to_blocks,
    block_to_block_type,
    )

class TestMarkdownExtraction(TestCase):
    def test_extract_markdown_images(self):
        text = """
        This is an image: ![My Image](path/to/image.jpg)
        This is another image: ![Image with [brackets]](path/to/image2.png)
        """
        expected_images = [
            ('My Image', 'path/to/image.jpg'),
            ('Image with [brackets]', 'path/to/image2.png')
        ]
        self.assertEqual(extract_markdown_images(text), expected_images)

    def test_extract_markdown_other_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        
        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected_images)

        #Test empty string
        self.assertEqual(extract_markdown_images(""), [])

        #Test text without images
        self.assertEqual(extract_markdown_images("No images here."), [])
    
    def test_extract_markdown_links(self):
        text = """
        This is a link: [Link Text](https://www.example.com)
        This is another link: [Link with spaces](another/link/path)
        """
        expected_links = [
            ('Link Text', 'https://www.example.com'),
            ('Link with spaces', 'another/link/path')
        ]
        self.assertEqual(extract_markdown_links(text), expected_links)

        # Test empty string
        self.assertEqual(extract_markdown_links(""), [])

        # Test text without links
        self.assertEqual(extract_markdown_links("No links here."), [])

    def test_extract_title(self):
        text = """# Hello, World!

        This is a sample markdown document.
        """

        self.assertEqual(extract_title(text), "Hello, World!")

    def test_extract_title_no_title(self):
        text = "No title to show"
        try:
            assert extract_title(text) == "No H1 Header found in markdown"
        except ValueError as e:
            assert str(e) == "No H1 Header found in markdown"
            
class TestMarkdownConvertion(TestCase):
    
    def test_markdown_to_blocks(self):
        markdown = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        expected_blocks = ['# This is a heading', 
                           'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                           '* This is the first list item in a list block', 
                           '* This is a list item', 
                           '* This is another list item']
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)
    
    def test_block_to_block_type(self):
        tests = [
            ('## Heading with text', 'heading'),
            ('#Invalid heading', 'paragraph'),
            ('```\ncode block\n```', 'code'),
            ('> Line 1\n> Line 2', 'quote'),
            ('* Item 1\n- Item 2', 'unordered list'),
            ('1. Item 1\n2. Item 2', 'ordered list'),
            ('1. Item 1\n2.Not a list', 'paragraph'),
            ('Plain text block', 'paragraph'),
            ]

        for text, expected in tests:
            block_type = block_to_block_type(text.strip())
            self.assertEqual(block_type, expected)
        

