#!/usr/bin/env python

import sys
import re
import os

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = filter(None, re.split('\W+', line))
    # write out word paired with count of 1

    # get the name of the input file (document)
    input_file = os.environ["mapreduce_map_input_file"]
    # extract the name of the document
    document_name = os.path.basename(input_file)

    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        # print('%s\t%s' % (word.lower(), 1))
        print('%s\t%s' % (word.lower() + "," + document_name, 1))
