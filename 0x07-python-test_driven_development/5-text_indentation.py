#!/usr/bin/python3
""" This module contains a function text_indentation(). for example
>>> text_indentation("i am Olalekan: Olalekan, do you really know me? me.")
i am olalekan:
<BLANKLINE>
Olalekan, do you really know me?
<BLANKLINE>
me.
"""

def text_indentation(text):
    """ This function indent text according ':?.' delimiter
    Args:
        text (string): The input text
    Raises:
        TypeError: if text is not a string
        """
    j = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    while j < len(text):
        if text[j] in ':?.':
            print(text[j], end='')
            print('\n')
            if text[j + 1] == ' ':
                j += 1
        else:
            print(text[j], end='')
        j += 1
