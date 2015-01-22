#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Dev Mehta / dpmehta02@gmail.com
Description: Processes yelp json/csv, munges and engineers features and outputs
    a csv suitable for Machine Learning. Requires a sentiment text file called
    AFINN-111.txt in the same directory:
    http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
Usage: python reviewProcessing.py <input_file>.json <output_file>
"""

import json
import re
import sys
import csv
from datetime import datetime

def processReviews(json_file):
    with open(sys.argv[2], 'w') as f:

        # Load sentiment score dict for lookups
        scores = {}
        afinnfile = open('AFINN-111.txt')
        for line in afinnfile:
            term, score = line.split("\t")
            scores[term] = int(score)

        # Write output file headers
        # TODO: there has to be a better way to handle this task
        f.write("user_id,votes_useful,days_active,comma_count,word_count,average_word_length,sentence_count,smilies,sentiment,character_count,user_average_stars,user_review_count,user_avg_votes_useful\n")

        user_data = {}
        if sys.argv[1] == 'yelp_training_set_review.json':
            for line in open("./yelp_training_set_json/yelp_training_set_user.json"):
                user_json = json.loads(line)
                user_average_stars = float(user_json['average_stars'])
                user_review_count = user_json['review_count']
                user_avg_votes_useful = float(user_json['votes']['useful']) / user_review_count
                user_data[user_json['user_id']] = (user_average_stars, user_review_count, user_avg_votes_useful)

        # Load and process the reviews
        for line in open(json_file):
            review_json = json.loads(line)

            # Set default values
            average_word_length, sentiment, votes_useful, sentence_count, smilies, character_count = 0, 0, 0, 0, 0, 0
            user_id = review_json['user_id']
            review_date = datetime.strptime(review_json['date'].encode('utf8'), "%Y-%m-%d") 

            # Assign date/votes useful based on Training data (if) or Test data (else)
            if review_json.get('votes'):
                votes_useful = review_json['votes']['useful']
                days_active = (datetime(2013, 01, 19) - review_date).days
            else:
                days_active = (datetime(2013, 03, 12) - review_date).days

            if review_json['text'] != '':
                utf_review = review_json['text'].encode('utf8')

                character_count, comma_count, word_count = len(utf_review), utf_review.count(','), len(utf_review.split())
                # This is naive: assumes each ., ? and ! ends a sentence
                sentence_count = utf_review.count('.') + utf_review.count('?') + utf_review.count('!')
                # Count happy emoticons
                smilies = utf_review.count(':)') + utf_review.count('=)') + utf_review.count(':-)')
                # Strip punctuation
                filtered = re.findall(r'\w+', utf_review)

                # Calculate sentiments
                for word in filtered:
                    # Only alphanumeric
                    if re.match("^[A-Za-z0-9_-]*$", word):
                        sentiment += scores.get(word, 0)
                try:
                    average_word_length = float(sum(len(word) for word in filtered)) / len(filtered)
                except ZeroDivisionError:
                    average_word_length == 0

            if user_id not in user_data:
                user_avg_stars, user_rev_count, user_average_votes_useful = 0, 0, 0
            else:
                user_avg_stars, user_rev_count, user_average_votes_useful = user_data[user_id][0], user_data[user_id][1], user_data[user_id][2]
            
            f.write("%s,%i,%i,%i,%i,%f,%i,%i,%i,%i,%.2f,%i,%.2f\n" % (user_id, votes_useful, days_active,
                                                                      comma_count, word_count, average_word_length,
                                                                      sentence_count, smilies, sentiment,
                                                                      character_count, 0, 0, 0))


if __name__ == '__main__':
    processReviews(sys.argv[1])
    print "Success!"
    return
