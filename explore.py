"""
=================================================
Data exploration
=================================================

In this file, we explore the data of the training set by extracting fields
(lang, access, name, agent),



Developed by Muhanad Shab Kaleia: m.kaleia@ou.edu
"""
print(__doc__)

import pandas as pd
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read the training set
train_1_path = BASE_DIR + '/train_1.csv'
df = pd.DataFrame.from_csv(train_1_path, index_col=None, encoding='utf-8')

# Add new fields, lang, article name, access, agent
df['agent'] = map(lambda v:v.split('_')[-1], df.Page)
df['access'] = map(lambda v:v.split('_')[-2], df.Page)
df['lang'] = map(lambda v: v.split('_')[-3].split('.')[0], df.Page)
df['article_name'] = map(lambda v: v.split('_')[0], df.Page)

df.to_csv(BASE_DIR + '/dataset.csv', encoding='utf-8')

