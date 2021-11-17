"""
class to reprasent positional index
"""
from typing import List


class PositionalIndex:
    """
    reprasent a position index of token in a document.
    """
    docid: int
    position_in_doc: List[int]

    def __init__(self, docid: int, position_in_doc: List[int]):
        self.docid = docid
        self.position_in_doc = position_in_doc
