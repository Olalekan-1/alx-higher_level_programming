#!/usr/bin/python3

def multiple_returns(sentence):
    first = sentence[0]
    if sentence == '':
        first = None
    return (len(sentence), first)
