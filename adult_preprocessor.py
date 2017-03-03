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
value_columns = ['age', 'fnlwgt', 'education-num' , 'capital-gain' ,'capital-loss', 'hours-per-week']
# quality_columns = [w.replace('[br]', '<br />') for w in words]
quality_columns = ['workclass', 'education','marital-status','occupation','relationship','race', 'sex', 'native-country','class']


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

    'atribute' : atribute,
    'min_value' : min_value,
    'max_value' : max_value,
    'average_value' : average_value,
    'standard_deviation' : standard_deviation
}

relatory_table = pd.DataFrame(relatory_table)
relatory_table.to_csv('adult/relatory_adult.csv')

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

    relatory_quality_table = {'class' : class_array , 'value' : value_array }
    relatory_quality_table = pd.DataFrame(relatory_quality_table)
    relatory_quality_table.to_csv('adult/class_' + name + '_table.csv')


#export data
df.to_csv('adult/proccessed_adult.csv')
