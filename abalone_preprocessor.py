import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# import matplotlib.pyplot as plt
    #
	# Sex		nominal			M, F, and I (infant)
	# Length		continuous	mm	Longest shell measurement
	# Diameter	continuous	mm	perpendicular to length
	# Height		continuous	mm	with meat in shell
	# Whole weight	continuous	grams	whole abalone
	# Shucked weight	continuous	grams	weight of meat
	# Viscera weight	continuous	grams	gut weight (after bleeding)
	# Shell weight	continuous	grams	after being dried
	# Rings		integer			+1.5 gives the age in years

DataLabels =["Sex","Length" ,"Diameter","Height","Whole_weight","Shucked_weight","Viscera_weight" ,"Shell_weight","Rings"]

filename = 'data/abalone.data'

#read data with labels
df = pd.read_csv(filename, header=None, names=DataLabels, sep=',', na_values=["?"], engine='python')
#drop null values
df = df.dropna(how='any')

#array of characterist column
value_columns = ["Length" ,"Diameter","Height","Whole_weight","Shucked_weight","Viscera_weight" ,"Shell_weight","Rings"]
# quality_columns = [w.replace('[br]', '<br />') for w in words]
quality_columns = ['Sex']


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
relatory_table.to_csv('abalone/relatory_abalone.csv')

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
    relatory_quality_table.to_csv('abalone/class_' + name + '_table.csv')


#export data
df = df.round(3)
df.to_csv('abalone/proccessed_abalone.csv')
