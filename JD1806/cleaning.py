#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:25:27 2018

@author: y
"""
import os
import pandas as pd
import numpy as np
import datetime
#import xgboost as xgb
from sklearn.model_selection import train_test_split

path='/Users/y/Downloads/JD/'
os.chdir(path)

sku = pd.read_csv('jdata_sku_basic_info.csv', )
#action = pd.read_csv('jdata_user_action.csv', parse_dates=['a_date'])
basic_info = pd.read_csv('jdata_user_basic_info.csv')
comment_score = pd.read_csv('jdata_user_comment_score.csv')
order = pd.read_csv('jdata_user_order.csv')


comment = pd.merge(basic_info, comment_score, on='user_id', how='left')
order = pd.merge(order, sku, on='sku_id', how='left')
comment = pd.merge(comment, sku, on='user_id', how='left')

comment = comment.sort_values(by=['user_id', 'comment_create_tm'])
comment['cm_year'] = comment['comment_create_tm'].apply(lambda x: x.year)
comment['cm_month'] = comment['comment_create_tm'].apply(lambda x: x.month)
comment['cm_day'] = comment['comment_create_tm'].apply(lambda x: x.day)