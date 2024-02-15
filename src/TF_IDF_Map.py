#!/usr/bin/env python

import sys

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into word-document pair and TF-IDF score
    word_document, tf_idf = line.split('\t', 1)

    print('%s\t%s' % (word_document, tf_idf))

