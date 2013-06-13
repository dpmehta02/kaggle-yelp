#!/usr/bin/env python

# @dpmehta02
# replace unnecessary characters (e.g., line breaks) for NLP

import re

def main():

  f = open('yelp_test_set_review.csv', 'r')
  temp = f.read().encode('utf-8', 'replace')
  data = re.sub(r'\r\n', ' ', temp)
  f.close()

  f = open('test_reviews_replaced.csv', 'w')
  f.write("%s" % data)
  f.close()

if __name__ == '__main__':
  main()