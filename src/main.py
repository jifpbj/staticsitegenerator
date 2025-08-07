from textnode import TextNode, TextType

def main():
    node = TextNode("anchor text", TextType.LINK, "https://example.com")
    print(node)

main()

