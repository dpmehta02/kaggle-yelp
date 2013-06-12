#!/usr/bin/env python

# @dpmehta02
# Count characters for each record in file
# USAGE: $ python countOccurrences.py <reviews_file>

import sys
import csv
import os

def main():

  f = open('test.csv', 'r')
  data = f.readlines()
  f.close()

  f = open('commmas.txt', 'w')

  for i in range(len(data)):
    if data[i] != []:
      f.write("%i\n" % data[i].count(","))


if __name__ == '__main__':
  main()