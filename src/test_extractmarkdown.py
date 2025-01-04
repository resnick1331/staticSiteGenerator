import re

from unittest import TestCase

from extractmarkdown import extract_markdown_images, extract_markdown_links

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