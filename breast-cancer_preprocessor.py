import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# import matplotlib.pyplot as plt

  #  1. Sample code number            id number
  #  2. Clump Thickness               1 - 10
  #  3. Uniformity of Cell Size       1 - 10
  #  4. Uniformity of Cell Shape      1 - 10
  #  5. Marginal Adhesion             1 - 10
  #  6. Single Epithelial Cell Size   1 - 10
  #  7. Bare Nuclei                   1 - 10
  #  8. Bland Chromatin               1 - 10
  #  9. Normal Nucleoli               1 - 10
  # 10. Mitoses                       1 - 10
  # 11. Class:


DataLabels =["id","Clump_Thickness" ,"Uniformity_of_Cell_Size","Uniformity_of_Cell_Shape","Marginal_Adhesion","Single_Epithelial_Cell_Size","Bare_Nuclei","Bland_Chromatin","Normal_Nucleoli","Mitoses","class"]

filename = 'data/breast-cancer-wisconsin.data'

#read data with labels
df = pd.read_csv(filename, header=None, names=DataLabels, sep=',', na_values=["?"], engine='python')
#drop null values
df = df.dropna(how='any')
df = df.drop('id', 1)

#array of characterist column
value_columns = ["Clump_Thickness" ,"Uniformity_of_Cell_Size","Uniformity_of_Cell_Shape","Marginal_Adhesion","Single_Epithelial_Cell_Size","Bare_Nuclei","Bland_Chromatin","Normal_Nucleoli","Mitoses"]
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

    'atribute' : atribute,
    'min_value' : min_value,
    'max_value' : max_value,
    'average_value' : average_value,
    'standard_deviation' : standard_deviation
}

relatory_table = pd.DataFrame(relatory_table)
relatory_table.to_csv('breast-cancer/relatory_breast-cancer.csv')

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
    relatory_quality_table.to_csv('breast-cancer/class_' + name + '_table.csv')


#export data
df.to_csv('breast-cancer/proccessed_breast-cancer.csv')
