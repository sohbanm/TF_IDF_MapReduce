#!/usr/bin/env python

import sys

# Initialize dictionaries to store TF and IDF values
tf_values = {}
idf_values = {}

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into key and value
    key, value = line.split('\t', 1)

    # Check if the key starts with 'document' (TF values) or 'word' (IDF values)
    check = key.split(',')

    if len(check) == 2:
    # if key.startswith('document'):
        # Extract word and document
        tf_value = float(value)
        word = check[0]

        # document_word, tf_value = key, float(value)
        # word = document_word.split('_')[1]

        # Store TF value
        if word not in tf_values:
            tf_values[word] = {}
        tf_values[word][check[1]] = tf_value
    else:
        # Store IDF value
        idf_values[key] = float(value)

# Compute TF-IDF for each word-document pair and emit
for word, documents in tf_values.iteritems():
    for document, tf_value in documents.iteritems():
        # Compute TF-IDF: TF * IDF
        tf_idf = tf_value * idf_values[word]
        print('%s\t%s' % (document, tf_idf))
