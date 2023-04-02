# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:56:01 2022

@author: ryan
"""

#import packages
import numpy as np
import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt

df=pd.read_excel('D:/product_information.xlsx')
df.shape
df = df.applymap(lambda s: s.upper() if type(s) == str else s) #turn string in df into upper case
df['Origin'].unique()
df['Origin']=df['Origin'].str.extract(r'((\b\w+)[\.?!\s]*$)')[0]
df['Origin'].unique()
Cat=df.Categories.unique().tolist()
Cat
counts=[]
labels=[]
for cat in range(len(Cat)):
 counts.append(df.groupby('Categories').get_group(Cat[cat])['Origin'].value_counts())
 counts
 labels.append(df.groupby('Categories').get_group(Cat[cat])['Origin'].unique().tolist())
 labels
 plt.pie(counts[cat], labels=labels[cat])



# Prepare data
#stacked bar chart for origin
df2=df.groupby(['Categories','Origin'])['Origin'].value_counts().unstack('Categories')
print(df2)
#Normalize Stacked bar chart
num_colors=len(df['Origin'].unique())
num_colors
df2 = df.groupby('Categories')['Origin'].value_counts().unstack('Origin').plot.bar(stacked=True,colormap='Paired')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.ylabel('Counts')
plt.title('Origin of Products in each Category', fontsize=22)
plt.colors('red')
plt.set_color_cycle([plt.cm.spectral(i) for i in np.linspace(0, 1, num_colors)])

df['Materials'].unique()