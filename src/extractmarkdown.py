import re

from textnode import TextNode, TextType

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)

    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text)

    return matches

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    
    raise ValueError("No H1 Header found in markdown")

def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.splitlines()

    for line in lines:
        if line != "":
            blocks.append(line.strip())

    return blocks

def block_to_block_type(block):
    if block.startswith("#"):
        heading_level = len(block) - len(block.lstrip("#"))
        if 1 <= heading_level <= 6:
            if (block.lstrip("#")).startswith(" "):
                return "heading"
    
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    
    lines = block.splitlines()
    if all(line.startswith(">") for line in lines):
        return "quote"
    
    if all(line.startswith(("- ", "* ")) for line in lines):
        return "unordered list"

    try:
        checked = []
        for i, line in enumerate(lines):
            if line[0] == str(i+1) and line.startswith(str(i+1) + ". "):
                checked.append(True)
            else:
                return "paragraph"
            
        if all(checked):
            return "ordered list"
    except ValueError:
        return "paragraph"
    
    return "paragraph"

text = "1. Item 1\n5. Item 2"

print(block_to_block_type(text))
    
