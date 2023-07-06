#!/usr/bin/python

import textwrap
mystr = """\
        Why, hello there
        wonderful stackoverfow people"""
print (textwrap.fill(textwrap.dedent(mystr)))
