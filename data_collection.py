#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:03:07 2021

@author: apple
"""

import Glassdoor_Scraper as gs
import pandas as pd


#This line will open a new chrome window and start the scraping.
df = gs.get_jobs("data scientist", 200, False,15)
df.to_csv('Glassdoor_data.csv', index = False)

df
"""

import Glassdoor_Scraper as gs 
import pandas as pd 

path = "/Users/apple/Desktop/Data Science/DS_Salary/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
"""

