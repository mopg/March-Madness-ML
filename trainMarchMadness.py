
############################## IMPORTS ##############################

from __future__ import division
import sklearn
import pandas as pd
import numpy as np
import collections
import os.path
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn import tree
from sklearn.model_selection import cross_val_score
from keras.utils import np_utils
from sklearn.neighbors import KNeighborsClassifier
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
import sys
from sklearn.ensemble import GradientBoostingRegressor
import math
import csv
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report
from sklearn.calibration import CalibratedClassifierCV
import urllib
from sklearn.svm import LinearSVC
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from datetime import datetime
import random
import pickle

############################## LOAD TRAINING SET ##############################

if os.path.exists("Data/PrecomputedMatrices/xTrain.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain.npy"):
	xAllData = np.load("Data/PrecomputedMatrices/xTrain.npy")
	yAllData = np.load("Data/PrecomputedMatrices/yTrain.npy")
	print ("Shape of xTrain:", xAllData.shape)
	print ("Shape of yTrain:", yAllData.shape)
else:
	print ('We need a training set! Run dataPreprocessing.py')
	sys.exit()

curYear = 2022

############################## LOAD CSV FILES ##############################

sample_sub_pd = pd.read_csv('Data/KaggleData/SampleSubmissionStage1.csv')
teams_pd = pd.read_csv('Data/KaggleData/Teams.csv')

############################## TRAIN MODEL ##############################

model = GradientBoostingRegressor(n_estimators=100, max_depth=5)

categories=['Wins','PPG','PPGA','PowerConf','3PG', 'APG','TOP','Conference Champ','Tourney Conference Champ',
           'Seed','SOS','SRS', 'RPG', 'SPG', 'Tourney Appearances','National Championships','Location']
accuracy=[]
numTrials = 1

# Train model and test it
X_train, X_test, Y_train, Y_test = train_test_split(xAllData, yAllData, test_size=.3)
startTime = datetime.now() # For some timing stuff
results = model.fit(X_train, Y_train)
preds = model.predict(X_test)
preds[preds < .5] = 0
preds[preds >= .5] = 1
localAccuracy = np.mean(preds == Y_test)
print ("Testing accuracy = " + str(localAccuracy))
print ("Time taken: " + str(datetime.now() - startTime))

with open('model.pkl', 'wb') as f:
	pickle.dump(model, f)
