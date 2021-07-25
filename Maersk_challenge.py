#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
import pandas as pd
import numpy as np

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, normalize, Normalizer

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm

from sklearn.model_selection import cross_val_score


#Loading Datasets
train_dataset = pd.read_csv('DS_ML Coding Challenge Dataset - Training Dataset.csv')
test_dataset = pd.read_csv('DS_ML Coding Challenge Dataset - Test Dataset.csv')

train_dataset = train_dataset[train_dataset['Sourcing Cost']<800]

train_dataset = train_dataset[np.logical_and(train_dataset['Sourcing Cost']>=0,train_dataset['Sourcing Cost']<=300)]

train_dataset['Quantity']=1
train_dataset=pd.pivot_table(train_dataset,values='Quantity',index=list(train_dataset.columns[:-1].values),aggfunc=np.sum).reset_index()


enc = OneHotEncoder(handle_unknown='ignore')
train_onehot=enc.fit_transform(train_dataset[train_dataset.columns[:6].values]).toarray()
test_onehot = enc.transform(test_dataset[test_dataset.columns[:6].values]).toarray()

enc2= OneHotEncoder(categories=[np.array([str(i) for i in range(1,13)])],handle_unknown='ignore')
train_onehot2=enc2.fit_transform(train_dataset['Month of Sourcing'].values.reshape(-1,1)).toarray()
test_onehot2 = enc2.transform(test_dataset['Month of Sourcing'].values.reshape(-1,1)).toarray()


# In[14]:


#Regrouping all features after onehot encoding
train_x=np.concatenate([train_onehot,train_onehot2,train_dataset[['Sourcing Cost']].values],axis=1)
train_y=train_dataset['Quantity'].values

test_x=np.concatenate([test_onehot,test_onehot2,test_dataset[['Sourcing Cost']].values],axis=1)


# In[15]:


scaler_x = MinMaxScaler().fit(train_x)
train_x = scaler_x.transform(train_x)
test_x = scaler_x.transform(test_x)

RFreg = RandomForestRegressor()

reg = RFreg.fit(train_x,train_y)


pre_y_test = reg.predict(test_x).astype(int)

print(pre_y_test)