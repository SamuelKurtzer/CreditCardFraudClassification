# %%
# Imports
## linear algebra
import numpy as np
## csv IO
import pandas as pd
## graph plotting
import matplotlib.pyplot as plt
## ???
import seaborn as sns
## timing
import time

# Classifiers
## DecisionTree
from sklearn.tree import DecisionTreeClassifier
## ???
from sklearn.linear_model import LogisticRegression
## SVM with kernal capabilitys
from sklearn.svm import SVC
## KNN
from sklearn.neighbors import KNeighborsClassifier
## DecisionTree
from sklearn.tree import DecisionTreeClassifier
## ???
from sklearn.ensemble import RandomForestClassifier
## Adaboost
from sklearn.ensemble import AdaBoostClassifier

# Data and result analysis
## classification accuracy scores
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report
## training and testing data generation
from sklearn.model_selection import KFold, StratifiedKFold

# %%
# Import Data
df = pd.read_csv('./creditcard.csv')

# %%
# Examine Data
## Examine the data for irregularitys
print(df.head())
print(df.describe())
if df.isnull().sum().max() > 0:
    print("Null values detected")
print(df.columns)

## Examine the class to class ratio
class0ratio = round(df['Class'].value_counts()[0]/len(df) * 100, 2)
class1ratio = round(df['Class'].value_counts()[1]/len(df) * 100, 2)
print('Class 0', class0ratio, '% of the dataset')
print('Class 1', class1ratio, '% of the dataset')

# %%
# Scale any part of the dataset that needs to be

# %%
# Split the testing data for later use
## get the X and Y values
X = df.drop('Class', axis=1)
y = df['Class']

## use 
skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)
for X_indices, Y_indicies in skf.split(X,y):
    print("Train:", train_index, "Test:", test_index)
    original_Xtrain, original_Xtest = X.iloc[train_index], X.iloc[test_index]
    original_ytrain, original_ytest = y.iloc[train_index], y.iloc[test_index]
##
