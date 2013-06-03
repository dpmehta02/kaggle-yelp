#!usr/bin/env python

# Dev Mehta @dpmehta02
# Linear regression with regularization and cross-validation

from sklearn import linear_model
import numpy as np

def main():
  # load data
  dataset = np.genfromtxt(open('train.csv','r'), delimiter=',', dtype='f8')[1:]    
  target = np.array([x[0] for x in dataset])
  inputs = np.array([x[1:] for x in dataset])

  # train ridge regression. Initialize lambda (AKA alpha) to 0, use 10-fold cross validation
  clf = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
  clf.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])       
  RidgeCV(alphas=[0.1, 1.0, 10.0], cv=10, fit_intercept=True, loss_func=None, normalize=False, score_func=None)

  # iterate through the training and test cross validation segments and
  # run the classifier on each one, aggregating the results into a list
  results = []
  for traincv, testcv in cv:
    probas = linearModel.fit(inputs[traincv], target[traincv]).predict_proba(inputs[testcv])
    results.append( logloss.llfun(target[testcv], [x[1] for x in probas]) )

  # mean of cross-validated results
  print "Results: " + str( np.array(results).mean() )
























if __name__=="__main__":
  main()