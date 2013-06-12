#!/usr/bin/env python

# @dpmehta02
# Count characters for each record in a csv file

import csv
import re

def main():

  f = open('train_plus_test_reviews.csv', 'r')
  data = f.readlines()
  f.close()

  f = open('commmas.txt', 'w')

  for i in range(len(data)):
    if data[i] != [] and data[i][0] == '\"':
      count = 0
      for char in data[i]:
        if char == ",":
          count += 1
      f.write("%i\n" % count)

  f.close()

if __name__ == '__main__':
  main()