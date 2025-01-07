import os
import shutil
import re

from textnode import TextNode, TextType

def generate_page(from_path, template_path = "",dest_path= ""):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    #Read markdown file
    try:
        with open(from_path, "r") as file:
            markdown_content = file.read()
            return markdown_content
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at {from_path}')
    
    #Read html template
    try:
        with open(template_path, "r") as file:
            html_content = file.read()
            return html_content
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at {template_path}')
    
    converted_content = 

current_dir = os.path.dirname(os.path.abspath(__file__)) 
src_dir = os.path.join(current_dir, '..', 'static/index.css')

print(generate_page(src_dir))