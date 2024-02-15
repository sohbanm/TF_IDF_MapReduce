#!/usr/bin/env python

from math import log
import sys

# Initialize variables
current_word = None
word_count = 0
total_documents = 20

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input
    word, _ = line.split('\t', 1)

    # Increment total documents
    # total_documents += 1

    # If the word is the same as the previous word
    if current_word == word:
        word_count += 1
    else:
        if current_word:
            # Calculate IDF for the current word
            idf = log(total_documents / word_count)

            # Output word and IDF
            print('%s\t%s' % (current_word, idf))
            word_count = 1
        else:
            word_count = 1

        # Update variables for the new word
        current_word = word

# Output IDF for the last word if needed
if current_word:
    idf = log(total_documents / word_count)
    print('%s\t%s' % (current_word, idf))
