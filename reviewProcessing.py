#!/usr/bin/env python

# @dpmehta02
# Output commas, words, and word length for each yelp review
# Usage: $ python reviewProcessing.py <input_file>.json <output_file>

import json
import re
import sys
import csv

def processReviews(json_file):
  
  # open output file
  f = open(sys.argv[2], 'w')
  
  # load a tab delimited dict of sentiment scores
  afinnfile = open('AFINN-111.txt')
  scores = {}
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)

  # write headers (ADD POOR GRAMMAR, POOR SPELLING?)
  f.write("comma_count,word_count,average_word_length,sentence_count,smilies,sentiment,character_count\n")
  
  # load/process the reviews
  for line in open(json_file):
    
    review_json = json.loads(line)
    
    # default values
    average_word_length = 0
    sentiment = 0
    
    # if the review isn't blank
    if review_json['text'] != '':
      
      # factored out for clarity
      utf_review = review_json['text'].encode('utf8')
      character_count = len(utf_review)
      comma_count = utf_review.count(',')
      word_count = len(utf_review.split())
      # naive: assumes each ., ? and ! ends a sentence
      sentence_count = utf_review.count('.') + utf_review.count('?') + utf_review.count('!')
      # happy emoticons!
      smilies = utf_review.count(':)') + utf_review.count('=)') + utf_review.count(':-)')
      # strip punctuation
      filtered = re.findall(r'\w+', utf_review)
      # look up/calculate sentiments
      for word in filtered:
        # only read alphanumeric words
        if re.match("^[A-Za-z0-9_-]*$", word):
          sentiment += scores.get(word, 0)

      # prevent divide-by-0 error
      if len(filtered) == 0:
        average_word_length == 0
      else:
        average_word_length = float(sum(len(word) for word in filtered))/len(filtered)
    
    f.write("%i,%i,%f,%i,%i,%i,%i\n" % (comma_count, word_count, average_word_length,
                                     sentence_count,smilies,sentiment,character_count))
  f.close()


def main():
  # process the reviews
  processReviews(sys.argv[1])

if __name__ == '__main__':
  main()
