#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:42:02 2021

@author: apple
"""

import numpy as np
import pandas as pd

# Reading data
data = pd.read_csv('gd_data.csv')

# Dropping rows where salary is not available as this is our dependent variable
data = data[data['Salary Estimate']!='-1']

# Cleaning salary column
salary = data['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary_clean = salary.apply(lambda x: x.replace('K','').replace('₹',''))
salary_clean1 = salary_clean.apply(lambda x: x.replace('Employer Provided Salary:',''))
salary_clean2 = salary_clean1.apply(lambda x: x.replace(',',''))


# Salary is given as range. So finding minimum and maximum salary from it.
min_sal = salary_clean2.apply(lambda x: x.split('-')[0])
max_sal = salary_clean2.apply(lambda x: x.split('-')[1] if len(x.split('-'))==2 else x.split('-')[0] )
data['min_salary'] = min_sal.apply(lambda x: x.rstrip())
data['max_salary'] = max_sal.apply(lambda x: x.lstrip())

# Typecasting
data['min_salary'] = data['min_salary'].astype(str).astype(int)
data['max_salary'] = data['max_salary'].astype(str).astype(int)
data['max_salary'].dtype

# Calculating avg salary 
data['avg_salary'] = (data['min_salary'] + data['max_salary']) / 2

# Company name also has rating in it, removing that
data['company_name'] = data.apply(lambda x: x['Company Name'] if x['Rating']==-1 else x['Company Name'][:-3] , axis=1)

# Calculating age of company
data['company_age'] = data['Founded'].apply(lambda x: x if x<0 else 2021-x )

# Finding which companies require python as necessary skill 
data['python'] = data['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
data['python'].value_counts()

# Finding which companies require SQL as necessary skill 
data['SQL'] = data['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
data['SQL'].value_counts()

# Finding which companies require Excel as necessary skill 
data['excel'] = data['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
data['excel'].value_counts()

# Finding which companies require Tableau as necessary skill 
data['tableau'] = data['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
data['tableau'].value_counts()


# Function to find various Titles offered by companies
def job_title(post):
    if 'analyst' in post.lower() or 'analytics' in post.lower():
        return 'Data Analyst'
    elif 'data scientist' in post.lower() or 'data science' in post.lower():
        return 'Data Scientist'
    elif 'data engineer' in post.lower():
        return 'Data Engineer'
    elif 'machine learning' in post.lower() or 'ai' in post.lower():
        return 'MLE'
    elif 'applied scientist' in post.lower():
        return 'Applied Scientist'
    else:
        return 'Other'
    
data['Post'] = data['Job Title'].apply(job_title)
data['Post'].value_counts()            


# Function to calculate seniority in Job title
def seniority(des):
    if 'sr' in des.lower() or 'senior' in des.lower() or 'sr.' in des.lower() or 'lead' in des.lower() or 'manager' in des.lower():
        return 'Senior'
    elif 'junior' in des.lower() or 'jr' in des.lower() or 'jr.' in des.lower() or 'associate' in des.lower() or 'trainee' in des.lower() or 'intern' in des.lower():
        return 'Junior'
    else:
        return 'Other'
    
data['Seniority'] = data['Job Title'].apply(seniority)
data['Seniority'].value_counts()


# Saving data as new csv file
data.to_csv('Data_cleaned.csv',index=False)















