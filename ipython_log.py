# IPython log file

import pandas
from pandas import read_csv
business = read_csv("/Users/devmehta/Kaggle/yelp/yelp_test_set/yelp_test_set_business.csv")
checkin = read_csv("/Users/devmehta/Kaggle/yelp/yelp_test_set/yelp_test_set_checkin.csv")
review = read_csv("/Users/devmehta/Kaggle/yelp/yelp_test_set/yelp_test_set_review.csv")
user = read_csv("/Users/devmehta/Kaggle/yelp/yelp_test_set/yelp_test_set_user.csv")
data_ur = pandas.merge(review, user, on='user_id', suffixes=('_left','_right'))
data_ur = pandas.merge(review, user, how='left', on='user_id', suffixes=('_left','_right'))
data_bc = pandas.merge(business, checkin, on='business_id', how='left', suffixes=('_left', '_right'))
data_urb = pandas.merge(data_ur, business, on='business_id', how='left', suffixes=('_left', '_right'))