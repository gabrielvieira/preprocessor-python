import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# import matplotlib.pyplot as plt

DataLabels =["age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
               "occupation", "relationship", "race", "sex", "capital-gain",
               "capital-loss", "hours-per-week", "native-country", "class"] 

filename = 'data/adult.data'

#read data with labels
df = pd.read_csv(filename, header=None, names=DataLabels, sep=',\s', na_values=["?"], engine='python')
#drop null values
df = df.dropna(how='any')

#array of characterist column
column_arr = ['age', 'fnlwgt', 'education-num' , 'capital-gain' ,'capital-loss', 'hours-per-week']

#maior, menor valor, media e desvio padrao
atribute = []
min_value = []
max_value = []
average_value = []
standard = []

for name in column_arr:
	print(name)

# normalize value column data || verificar education-num
scaler = MinMaxScaler()
df[column_arr] = scaler.fit_transform(df[column_arr])
# df[['age']] = scaler.fit_transform(df[['age']])

#replace class values

#export data
df.to_csv('proccessed_adult.csv')

#plot
# plt.hist(df['age'], 30, normed=True) #Number of breaks is 30
# plt.show()
