import sys
import os
print("hello world")
from textnode import TextNode, TextType

from copy_content import copy_directory_content

def main():
    #text_node = TextNode("This is a test, I repeat, this is a test", TextType.ITALIC,"https://www.boot.dev")
    #print(text_node)

    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the paths to the source and destination directories
    src_dir = os.path.join(current_dir, '..', 'static')  # Go one level up from the script's directory
    dest_dir = os.path.join(current_dir, '..', 'public')

    copy_directory_content(src_dir,dest_dir)

if __name__ == "__main__":
    main()

