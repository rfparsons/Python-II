'''File: regex.py
Author: Bobby Parsons
Date: 9/7/21

Demonstrates the use of reguilar expressions
'''

import re

if (__name__ == '__main__'):
    dune_quote = '“I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.” – Frank Herbert, Dune'
    

    f = re.findall('f', dune_quote, flags=re.IGNORECASE)
    print(f)
    print(len(f))

    f2 = re.findall('f\w*\s', dune_quote, flags=re.IGNORECASE)
    print(f2)
    print(len(f2))

    nots = re.findall('not[\s.,!;?)]', dune_quote, flags=re.IGNORECASE) 
    #only need to cover the whitespace but might as well get them all
    print(nots)
    print(len(nots))

    dune_quote = re.sub("I ", "You ", dune_quote,flags=re.IGNORECASE)
    dune_quote = re.sub("my ", "your ", dune_quote,flags=re.IGNORECASE)
    dune_quote = re.sub("me ", "you ", dune_quote,flags=re.IGNORECASE)
    dune_quote = re.sub("me.", "you.", dune_quote,flags=re.IGNORECASE)
    print(dune_quote)