from markdown_blocks import block_to_block_type, BlockType
from splitnodes import markdown_to_blocks, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node
import textwrap

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def list_to_children(text):
    split_nodes = text.split("\n")
    if all(node.startswith("- ") or node.startswith("* ") for node in split_nodes):
        html_nodes = [LeafNode("li", node[2:]) for node in split_nodes if node.startswith("- ") or node.startswith("* ")]
    else:
        html_nodes = [LeafNode("li", node[3:]) for node in split_nodes if node.startswith("1. ") or node.startswith("2. ")]
    return html_nodes




def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in blocks:
        type_of_block = block_to_block_type(block)
        if type_of_block == BlockType.PARAGRAPH:
            block = " ".join(block.split())
            if block != "":
                node_list.append(ParentNode("p", text_to_children(block)))
            else:
                continue
        elif type_of_block == BlockType.HEADING:
            level = block.count("#")
            node_list.append(ParentNode(f"h{level}", text_to_children(block)))
        elif type_of_block == BlockType.QUOTE:
            node_list.append(ParentNode("blockquote", text_to_children(block)))
        elif type_of_block == BlockType.UNORDERED_LIST:
            node_list.append(ParentNode("ul", list_to_children(block)))
        elif type_of_block == BlockType.ORDERED_LIST:
            node_list.append(ParentNode("ol", list_to_children(block)))
        elif type_of_block == BlockType.CODE:
            lines = block.split('\n')
            code_content = '\n'.join(lines[1:-1]) + '\n'
            code_content = textwrap.dedent(code_content)
            node_list.append(ParentNode("pre", [LeafNode("code", code_content)]))
        else:
            raise ValueError(f"Unknown block type: {type_of_block}")
            return None
    return ParentNode("div", node_list)





