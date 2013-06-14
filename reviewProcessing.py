#!/usr/bin/env python

# @dpmehta02
# Output commas, words, and word length for each yelp review
# Usage: $ python reviewProcessing.py <input_file>.json <output_file>

import json
import re
import sys

def processReviews(json_file):
  
  # open output file
  f = open(sys.argv[2], 'w')
  
  # write headers
  f.write("comma_count,word_count,average_word_length,sentence_count,smilies\n")
  
  # load/process the reviews
  for line in open(json_file):
    
    review_json = json.loads(line)
    average_word_length = 0
    
    # if the review isn't blank
    if review_json['text'] != '':
      
      # factored out for clarity
      utf_review = review_json['text'].encode('utf8')
      
      comma_count = utf_review.count(',')
      word_count = len(utf_review.split())
      # naive: assumes each ., ? and ! ends a sentence
      sentence_count = utf_review.count('.') + utf_review.count('?') + utf_review.count('!')
      
      smilies = utf_review.count(':)') + utf_review.count('=)') + utf_review.count(':-)')
      # strip punctuation
      filtered = re.findall(r'\w+', utf_review)
      # prevent divide-by-0 error
      if len(filtered) == 0:
        average_word_length == 0
      else:
        average_word_length = float(sum(len(word) for word in filtered))/len(filtered)
    
    f.write("%i,%i,%f,%i,%i\n" % (comma_count, word_count, average_word_length,sentence_count,smilies))
  f.close()


def main():
  # process the reviews
  processReviews(sys.argv[1])

if __name__ == '__main__':
  main()
