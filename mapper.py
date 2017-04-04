#!/usr/bin/env python
import csv
import sys
import re

# input comes from STDIN (standard input)

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line=re.sub(r'".*"',' ',line)
    # split the line into words
    words = line.split(',')
    # increase counters
    count=0
    if words[0]!='DATE':
        for word in words:
                count=count+1
        #if word=="":
                #word=word.replace("","new")
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
                if count >= 25 and word:
                        print '%s\t%s' % (word, 1)
