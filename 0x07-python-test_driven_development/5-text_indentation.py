#!/usr/bin/python3
""" This module contains a function text_indentation(). for example
>>> text_indentation("i am Olalekan: Olalekan, do you really know me? me.")
i am Olalekan:
<BLANKLINE>
Olalekan, do you really know me?
<BLANKLINE>
me."""


def text_indentation(text):
    """ This function indent text according ',:?.' delimiter
    Args:
        text (string): The input text
    Raises:
        TypeError: if text is not a string
        """
    if type(text) is not str:
        raise TypeError("text must be a string")

    delimiter_chars = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        if text[i] in delimiter_chars:
            result += text[i]
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
            result += '\n\n'
        else:
            result += text[i]
        i += 1

    if result.endswith('\n\n'):
        result = result[:-2]

    print(result, end='')
