from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if extract_markdown_images(old_node.text) == []:
            new_nodes.append(old_node)
            continue
        extracted_images = extract_markdown_images(old_node.text)
        split_nodes = []
        sections = old_node.text
        for img_link in extracted_images:
            sections = sections.split(f"![{img_link[0]}]({img_link[1]})", 1)
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(img_link[0], TextType.IMAGE, img_link[1]))
            sections = sections[1]
        if sections != "":
            split_nodes.append(TextNode(sections, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if extract_markdown_links(old_node.text) == []:
            new_nodes.append(old_node)
            continue
        extracted_links = extract_markdown_links(old_node.text)
        split_nodes = []
        sections = old_node.text
        for link in extracted_links:
            sections = sections.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            sections = sections[1]
            split_nodes.append(TextNode(link[0], TextType.IMAGE, link[1]))
        if sections != "":
            split_nodes.append(TextNode(sections, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    """
    Convert a text string to a list of TextNode objects.
    This function is used to convert the text content of a node to a list of TextNode objects.
    """
    original_node = [TextNode(text, TextType.TEXT)]
    italics = split_nodes_delimiter(original_node, "_", TextType.ITALIC)
    bold = split_nodes_delimiter(italics, "**", TextType.BOLD)
    code = split_nodes_delimiter(bold, "`", TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    return links

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
