# =====  Eksplorasi Data: Memahami Data dengan Statistik - Part 1  =====
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
print('Shape dataset:', dataset.shape)
print('\nLima data teratas:\n', dataset.head())
print('\nInformasi dataset:')
print(dataset.info())
print('\nStatistik deskriptif:\n', dataset.describe())

# =====  Eksplorasi Data: Memahami Data dengan Statistik - Part 2  =====
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
dataset_corr = dataset.corr()
print('Korelasi dataset:\n', dataset.corr())
print('Distribusi label (Revenue):\n', dataset['Revenue'].value_counts())
#Tugas praktek
print('Korelasi BounceRates-ExitRates:', dataset_corr.loc['BounceRates','ExitRates'])
print('Korelasi Revenue-PageValues:', dataset_corr.loc['Revenue','PageValues'])
print('Korelasi TrafficType-Weekend:', dataset_corr.loc['TrafficType','Weekend'])

# =====  Eksplorasi Data: Memahami Data dengan Visual  =====
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
#checking the Distribution of customers on Revenue
plt.rcParams['figure.figsize']=(12,5)
plt.subplot(1,2,1)
sns.countplot(dataset['Revenue'], palette='pastel')
plt.title('Buy or Not', fontsize=20)
plt.xlabel('Revenue or not', fontsize=14)
plt.ylabel('count', fontsize=14)
#checking the Distribution of customers on Weekend
plt.subplot(1,2,2)
sns.countplot(dataset['Weekend'], palette='inferno')
plt.title('Purchase on Weekend', fontsize=20)
plt.xlabel('Weekend or not', fontsize=14)
plt.ylabel('count', fontsize=14)
plt.show()

# =====  Tugas Praktek  =====
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
#visualizing the distribution of customers around the Region
plt.hist(dataset['Region'], color = 'lightblue')
plt.title('Distribution of Customers', fontsize = 20)
plt.xlabel('Region Codes', fontsize = 14)
plt.ylabel('Count Users', fontsize = 14)
plt.show()

# =====  Data Pre-processing: Handling Missing Value - Part 1  =====
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
#checking missing value for each feature  
print('Checking missing value for each feature:')
print(dataset.isnull().sum())
#Counting total missing value
print('\nCounting total missing value:')
print(dataset.isnull().sum().sum())

# =====  Data Pre-processing: Handling Missing Value - Part 2  =====
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
#Drop rows with missing value   
dataset_clean = dataset.dropna()  
print('Ukuran dataset_clean:', dataset_clean.shape)

# =====  Data Pre-processing: Handling Missing Value - Part 3  =====
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
print("Before imputation:")
#Checking missing value for each feature  
print(dataset.isnull().sum())
#Counting total missing value  
print(dataset.isnull().sum().sum())
print("\nAfter imputation:")
#Fill missing value with mean of feature value  
dataset.fillna(dataset.mean(), inplace = True)
#Checking missing value for each feature  
print(dataset.isnull().sum())
#Counting total missing value  
print(dataset.isnull().sum().sum())

# =====  Tugas Praktek  =====
import pandas as pd
dataset1 = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
print("Before imputation:")
#Checking missing value for each feature  
print(dataset1.isnull().sum())
#Counting total missing value  
print(dataset1.isnull().sum().sum())
print("\nAfter imputation:")
#Fill missing value with median of feature value  
dataset1.fillna(dataset1.median(), inplace = True)
#Checking missing value for each feature  
print(dataset1.isnull().sum())
#Counting total missing value  
print(dataset1.isnull().sum().sum())

# =====  Tugas Praktek  =====
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
dataset.fillna(dataset.mean(), inplace = True)
from sklearn.preprocessing import MinMaxScaler  
#Define MinMaxScaler as scaler  
scaler = MinMaxScaler()  
#list all the feature that need to be scaled  
scaling_column = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues']
#Apply fit_transfrom to scale selected feature  
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])
#Cheking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min','max']])

# =====  Data Pre-processing: Konversi string ke numerik  =====
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
dataset.fillna(dataset.mean(), inplace = True)
import numpy as np
from sklearn.preprocessing import LabelEncoder
#Convert feature/column 'Month'
LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])
print(LE.classes_)
print(np.sort(dataset['Month'].unique()))
print('')
#Convert feature/column 'VisitorType'
LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])
print(LE.classes_)
print(np.sort(dataset['VisitorType'].unique()))
