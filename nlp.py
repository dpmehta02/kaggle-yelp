#!/usr/bin/env python

# @dpmehta02
# Analyze Yelp reviews for sentiment (negativity/positivity)

#import nltk
import textmining

def main():
  
  test_file = open("test_file.txt", "w")
  # Initialize class to create term-document matrix
  tdm = textmining.TermDocumentMatrix()
  
  for line in open('test_reviews.txt', 'r'):
    # Add the documents
    tdm.add_doc(line)
    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document.
    tdm.write_csv('matrix.csv', cutoff=2)

'''
SAMPLE - PRINT ALL WORDS THAT END WITH ING
def main():
  test_file = open("test_file.txt", "w")
  for line in open('test_reviews.txt', 'r'):
    for word in line.split():
      if word.endswith('ing'):
        test_file.write("%s\n" % word)


SENTIMENT ANALYSIS
import sys
import csv
import re

def main():

  # load a tab delimited dict of sentiment scores
  afinnfile = open(sys.argv[1])
  scores = {}
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)

  csv_reviews = csv.reader(open(sys.argv[2], 'rb'))
  f = open('review_sentiments.txt', 'w')

  # load each tweet as json
  for line in csv_reviews:
    score = 0
    if line != []:
      text_line = line[0].split()
      for word in text_line:
        # only read alphanumeric words
        if re.match("^[A-Za-z0-9_-]*$", word):
          score += scores.get(word, 0)
    f.write("%i\n" % score)
'''

if __name__ == '__main__':
  main()