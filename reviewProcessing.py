#!/usr/bin/env python

# @dpmehta02
# Output commas, words, and word length for each yelp review
# Usage: $ python reviewProcessing.py <output_file> <input_file>.json

import json
import re
import sys

def main():
  
  # output file
  f = open(sys.argv[1], 'w')
  # headers
  f.write("comma_count,word_count,average_word_length\n")

  # load the reviews
  for line in open(sys.argv[2]):
    review_json = json.loads(line)
    average_word_length = 0
    if review_json['text'] != '':
      comma_count = review_json['text'].encode('utf8').count(',')
      word_count = len(review_json['text'].encode('utf8').split())

      filtered = re.findall(r'\w+', review_json['text'].encode('utf8'))
      if len(filtered) == 0:
        average_word_length == 0
      else:
        average_word_length = float(sum(len(word) for word in filtered))/len(filtered)
    
    f.write("%i,%i,%f\n" % (comma_count, word_count, average_word_length))
  f.close()

if __name__ == '__main__':
  main()
