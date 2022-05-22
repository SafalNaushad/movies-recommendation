# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:27:26 2022

@author: Safal
"""


import csv
import pandas as pd
import random
New=[]
with open('movieR.csv','r') as csvfile:
    readCSV = csv.reader(csvfile)
    New.append(random.choice(list(readCSV)))
print(New[0][0])
        
        