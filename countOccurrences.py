#!/usr/bin/env python

# @dpmehta02
# Count characters for each record in file
# USAGE: $ python countOccurrences.py <reviews_file>
# Generates scores in review_sentiments.txt

import sys
import csv
import re

def main():

  content = open("test.csv", "r").read().replace('\r\n','\n')

  with open("processed_comments.csv", "w") as g:
    g.write(content)

  # open files for reading and writing
  f = open('review_commas.txt', 'w')
  csv_reviews = csv.reader(open('processed_comments.csv', 'rb'), quoting=csv.QUOTE_NONE)
  
  # count commas
  for line in csv_reviews:
    if line != []:
      count = 0
      for c in line:
        if c == ',':
          count += 1
      f.write("%i\n" % count)

if __name__ == '__main__':
  main()