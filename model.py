#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:07:23 2021

@author: apple
"""

# More that 70% of salary data scraped from glassdoor was missing which were filled with mean salary values from a rough  
# google search. Hence in a way this data is made up so we cannot expect high accuracy from models. Even 50% accuracy 
# would be suprising.


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('/Users/apple/Desktop/Data Science/DS_Salary/Data_cleaned.csv')

data.columns

data_model = data[[ 'avg_salary','Job Title','Rating', 'Location', 'Size',
                   'Type of ownership','Industry', 'Sector', 'Revenue', 
                   'company_name', 'company_age', 'python',
                   'SQL', 'excel','tableau', 'Post', 'Seniority']]

data_dummies = pd.get_dummies(data_model)

inputs = data_dummies.drop('avg_salary',axis=1)
target = data_dummies['avg_salary']

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(inputs)
inputs_scaled = scaler.transform(inputs)


X_train, X_test, y_train, y_test = train_test_split( inputs_scaled, target, test_size=0.20, 
                                                   random_state=23)
# Linear regression
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train,y_train)

prediction = reg.predict(X_train)
test_predictions = reg.predict(X_test)


from sklearn.model_selection import cross_val_score
np.mean(cross_val_score(reg, X_test, y_test, cv=3, scoring='neg_mean_squared_error'))



# Logistic regression
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(solver='lbfgs', max_iter=1000)
logreg.fit(X_train, y_train.astype('int'))
y_pred = logreg.predict(X_test)


import sklearn.metrics as sm
print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred), 2)) 
print("R2 score =", round(sm.r2_score(y_test, y_pred), 2))


# Support vector regression
from sklearn.svm import SVR
svr = SVR()
svr.fit(X_train, y_train)
y_pred_svr = svr.predict(X_test)
np.mean(cross_val_score(svr, X_test, y_test, cv=3, scoring='neg_mean_squared_error'))

# Lasso regression
from sklearn import linear_model
las = linear_model.Lasso(alpha=0.1,max_iter=2000)
las.fit(X_train,y_train)
y_pred_las = las.predict(X_test)
np.mean(cross_val_score(las, X_test, y_test, cv=3, scoring='neg_mean_squared_error'))

# Random forest regression
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=4, random_state=0)
rf.fit(X_train,y_train)
y_pred_rf = rf.predict(X_test)
np.mean(cross_val_score(rf, X_test, y_test, cv=3, scoring='neg_mean_squared_error'))

# Optimizing random forest
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,200,10),'criterion':('mse','mae'),'max_depth':(3,4,5),'max_features':('auto','sqrt','log2')}
gs = GridSearchCV(rf, parameters, cv=3,scoring='neg_mean_absolute_error')
gs.fit(X_train,y_train)

gs.best_score_
gs.best_params_

# Testing on best parameters
rf1 = RandomForestRegressor(criterion = 'mae', max_depth = 5,max_features = 'auto', n_estimators= 30)
rf1.fit(X_train,y_train)
y_pred_rf1 = rf1.predict(X_test)
np.mean(cross_val_score(rf1, X_test, y_test, cv=3, scoring='neg_mean_squared_error'))

