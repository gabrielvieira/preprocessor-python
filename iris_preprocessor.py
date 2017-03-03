import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# import matplotlib.pyplot as plt

DataLabels =["sepal_length","sepal_width" ,"petal_length","petal_width","class"]

filename = 'data/iris.data'

#read data with labels
df = pd.read_csv(filename, header=None, names=DataLabels, sep=',', na_values=["?"], engine='python')
#drop null values
df = df.dropna(how='any')

#array of characterist column
value_columns = ['sepal_length','sepal_width' ,'petal_length','petal_width']
# quality_columns = [w.replace('[br]', '<br />') for w in words]
quality_columns = ['class']


#maior, menor valor, media e desvio padrao
atribute = []
min_value = []
max_value = []
average_value = []
standard_deviation = []

for index, name in enumerate(value_columns):

    atribute.insert( index, name)
    min_value.insert( index, df[name].min())
    max_value.insert( index, df[name].max())
    average_value.insert( index, df[name].mean())
    standard_deviation.insert( index, df[name].std())


relatory_table = {

    'Atributo' : atribute,
    'Menor Valor' : min_value,
    'Maior Valor' : max_value,
    'Média' : average_value,
    'Desvio Padrão' : standard_deviation
}

relatory_table = pd.DataFrame(relatory_table)
relatory_table = relatory_table.round(3)
relatory_table.to_csv('iris/relatory_iris.csv')

# normalize value column data || verificar education-num
scaler = MinMaxScaler()
df[value_columns] = scaler.fit_transform(df[value_columns])

#replace class values
for index, name in enumerate(quality_columns):

    #get unique values
    unique_values = df[name].unique()
    class_array = []
    value_array = []

    for index_, unique_name in enumerate(unique_values):
        df[name] = df[name].replace([unique_name], index_)
        class_array.insert( index_, unique_name)
        value_array.insert( index_, index_)

    relatory_quality_table = {" " + name : class_array , 'Valor' : value_array }
    relatory_quality_table = pd.DataFrame(relatory_quality_table)
    relatory_quality_table.to_csv('iris/class_' + name + '_table.csv')


#export data
df = df.round(3)
df.to_csv('iris/proccessed_iris.csv')
