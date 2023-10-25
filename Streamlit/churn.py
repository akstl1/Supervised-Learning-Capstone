# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 23:15:21 2023

@author: allan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,plot_confusion_matrix,accuracy_score,precision_score,recall_score,f1_score
from sklearn.preprocessing import OneHotEncoder,MinMaxScaler
from sklearn.inspection import permutation_importance

from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import RFECV

from sklearn.linear_model import LogisticRegression

import joblib


df = pd.read_csv('DATA/Telco-Customer-Churn.csv')
df.drop('customerID', axis=1, inplace=True)

def tenure_cohort(tenure):
    if tenure<13:
        return '0-12 months'
    elif tenure<25:
        return '12-24 months'
    elif tenure<49:
        return '24-48 months'
    return 'over 48 months' 

df['tenure_cohort'] = df['tenure'].apply(tenure_cohort)
X=df.drop('Churn', axis=1)
y=df['Churn']
X = pd.get_dummies(X,drop_first=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, plot_confusion_matrix,classification_report

rf_model = RandomForestClassifier()
param_grid = {'n_estimators':[50,100], 'max_depth': [2,4,6,8,10]}
grid = GridSearchCV(rf_model,param_grid)
grid.fit(X_train, y_train)
grid.best_params_


joblib.dump(grid, "churn_model.joblib")

