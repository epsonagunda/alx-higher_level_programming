#!/usr/bin/python3
"""
text identation module:
indents text
useful
"""


def text_indentation(text):
    """text must be a string, There should be no space
    at the beginning
    or at the end of each printed line.
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
