from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.search(r'^#{1,6}', block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") or line.startswith("* ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(lines[i].startswith(f"{i+1}.") for i in range(len(lines))):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

