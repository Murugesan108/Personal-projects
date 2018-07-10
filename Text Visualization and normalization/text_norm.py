# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:04:37 2017

@author: Arvind
"""

import os
import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt

os.chdir('C:\\Users\\Arvind\\Desktop\\kaggle\\Text normalization')
os.getcwd()

train_text = pd.read_csv("en_train.csv")

#Get the value of all non-null value counts

train_text.isnull().sum(axis = 0)
train_text.count()

train_text.dtypes

train_text.head()

train_text['class'].value_counts()

#Create a change column 
train_text['change'] = train_text['before'] != train_text['after']
train_text['change'].value_counts()


#Work on a smaple of the entire data frame

random.seed(0)
train_sample = train_text.sample(frac = 0.1)


class_value = train_sample['class'].value_counts()

#How many entries per category
train_sample['class'].value_counts().plot(kind  = "bar")
np.log(train_sample['class'].value_counts()).plot(kind  = "bar")


agg_count = train_sample.loc[:,['class','change']].groupby(['class','change'])['class'].count()


train_sample['change'].value_counts()

train_sample = train_sample.reset_index()
