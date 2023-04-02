# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:29:13 2022

@author: ryan
"""


#import packages
import numpy as np
import random
import pandas as pd
import plotly.express as px
import mlxtend
from mlxtend.frequent_patterns import fpgrowth, association_rules

#building random true false matrix with m rows n columns min of p and max of p true 
def boolmatrix(m,n):
 a = (np.random.randint(0, m, size=n) == np.arange(m).reshape(-1, 1)).astype(int)
 return a

def randbin(m, n, p, q):
    # output to assign ones into
    result = np.zeros((m, n), dtype=bool)
    # simulate sampling with replacement in one axis
    col_ind = np.argsort(np.random.random(size=(m, n)), axis=1)
    # figure out how many samples to take in each row
    count = np.random.randint(p, q + 1, size=(m, 1))
    # turn it into a mask over col_ind using a clever broadcast
    mask = np.arange(n) < count
    # apply the mask not only to col_ind, but also the corresponding row_ind
    col_ind = col_ind[mask]
    row_ind = np.broadcast_to(np.arange(m).reshape(-1, 1), (m, n))[mask]
    # Set the corresponding elements to 1
    result[row_ind, col_ind] = 1
    return result
def crazyshuffle(arr):
     x, y = arr.shape
     rows = np.indices((x,y))[0]
     cols = [np.random.permutation(y) for _ in range(x)]
     return arr[rows, cols]
    
# Loading the Data
df=pd.read_excel('D:/product_information.xlsx')
products=list(df['Product Name'].unique())
type(products)
len(products)
matrix=randbin(5000,401,1,8)
np.random.shuffle(matrix.T)                  
trans=pd.DataFrame(matrix,columns=products)
trans.to_csv('D:/trans.csv')
#add counts of true in each column
count=[]
for column in trans:
     count.append(trans[column].values.sum())
trans.loc[len(trans)]=count
trans.columns
trans.shape
# select top 50 items
df_table = trans.sort_values(by=10000,axis=1,ascending=False)
df_table.to_csv('D:/table.csv')
df_table.shape

top50 = df_table.columns[0:50]
top50
dataset= df_table.iloc[:,0:50]
dataset.shape
#implementing FP-Growth Algorithm
res=fpgrowth(dataset.loc[0:9999,:],min_support=0.013, use_colnames=True)

# printing top 10
# Sort values based on confidence
res.sort_values("support",ascending=False)
# printing association rules
res
