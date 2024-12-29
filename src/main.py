print("hello world")
from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is a test, I repeat, this is a test", TextType.ITALIC,"https://www.boot.dev")
    print(text_node)

main()
