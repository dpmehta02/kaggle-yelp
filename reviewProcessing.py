#!/usr/bin/env python

########################################################################
# @dpmehta02 dpmehta02@gmail.com
# Processes yelp json/csv, analyzes text, generates csv
# Usage: $ python reviewProcessing.py <input_file>.json <output_file>
########################################################################

from datetime import datetime
import json
import re
import sys
import csv

def processReviews(json_file):
  # open output file
  f = open(sys.argv[2], 'w')
  
  # load sentiment score dict
  afinnfile = open('AFINN-111.txt')
  scores = {}
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)

  # write headers (ADD POOR GRAMMAR, POOR SPELLING?, user name normal?)
  f.write("user_id,votes_useful,days_active,comma_count,word_count,average_word_length,sentence_count,smilies,sentiment,character_count,user_average_stars,user_review_count,user_avg_votes_useful\n")

  # user_data[user_id] = (average_stars, review_count, avg_votes_useful)
  user_data = {}

  # temporarily held out of calcuations
  if sys.argv[1] == 'yelp_training_set_review.json':
    # load/process user data
    for line in open("./yelp_training_set_json/yelp_training_set_user.json"):
      user_json = json.loads(line)
      user_average_stars = float(user_json['average_stars'])
      user_review_count = user_json['review_count']
      user_avg_votes_useful = float(user_json['votes']['useful']) / user_review_count
      user_data[user_json['user_id']] = (user_average_stars, user_review_count, user_avg_votes_useful)

  '''
  if sys.argv[1] == 'yelp_test_set_review.json':
    # load/process user data
    for line in open("./yelp_test_set_json/yelp_test_set_user.json"):
      user_test_json = json.loads(line)
      user_average_stars = float(user_test_json['average_stars'])
      user_review_count = user_test_json['review_count']
      user_avg_votes_useful = 0
      user_data[user_test_json['user_id']] = (user_average_stars, user_review_count, user_avg_votes_useful)
  '''
      
  # load/process the reviews
  for line in open(json_file):
    review_json = json.loads(line)

    # default values
    average_word_length = 0
    sentiment = 0
    votes_useful = 0
    sentence_count = 0
    smilies = 0
    character_count = 0
    user_id = review_json['user_id']

    review_date = datetime.strptime(review_json['date'].encode('utf8'),"%Y-%m-%d")
    
    # training set
    if review_json.get('votes'):
      votes_useful = review_json['votes']['useful']
      days_active = (datetime(2013, 01, 19) - review_date).days

    # test set
    else:
      days_active = (datetime(2013, 03, 12) - review_date).days

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

    if user_id not in user_data:
      user_avg_stars = 0
      user_rev_count = 0
      user_average_votes_useful = 0
    else:
      user_avg_stars = user_data[user_id][0]
      user_rev_count = user_data[user_id][1]
      user_average_votes_useful = user_data[user_id][2]

    f.write("%s,%i,%i,%i,%i,%f,%i,%i,%i,%i,%.2f,%i,%.2f\n" % (user_id, votes_useful, days_active,
                                                 comma_count, word_count, average_word_length,
                                                 sentence_count, smilies, sentiment, 
                                                 character_count, 0,0,0))
  f.close()


def main():
  processReviews(sys.argv[1])
  return 0


if __name__ == '__main__':
  main()
