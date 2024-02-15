#!/usr/bin/env python

import sys

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into word-document pair
    word_document, _ = line.split('\t', 1)

    # Extract the word from the word-document pair
    word = word_document.split(',')[0]

    # Emit word and count of 1
    print('%s\t%s' % (word, 1))
