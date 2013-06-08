#!/usr/bin/env python

# @dpmehta02
# Create bag-of-words matrix

import textmining

def main():
  # Initialize
  tdm = textmining.TermDocumentMatrix()
  
  for line in open('train_plus_test_reviews.csv', 'r'):
    # Add each review
    tdm.add_doc(line)
    # Write out the matrix to a csv file. Cutoff is words
    # which appear in x or more documents
    tdm.write_csv('matrix.csv', cutoff=2)

if __name__ == '__main__':
  main()