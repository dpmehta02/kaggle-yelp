#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Dev Mehta / dpmehta02@gmail.com
Description: Create bag-of-words (Term-Document) matrix from a csv of strings
Usage: python generateTDM.py
"""

import textmining

def main():
    # This file should only include rows of text. Be careful of mid-string
    # linebreaks!
    with open("train_plus_test_reviews.csv", "r") as f:
        tdm = textmining.TermDocumentMatrix()
        for line in f:
            tdm.add_doc(line)
            # Only include words which appear in 2+ documents
            tdm.write_csv('matrix.csv', cutoff=2)

if __name__ == '__main__':
  main()