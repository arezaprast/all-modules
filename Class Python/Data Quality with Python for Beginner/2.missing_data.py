import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')
# Check kolom yang memiliki missing data
print('Check kolom yang memiliki missing data:')
print(retail_raw.isnull().any())
# Filling the missing value (imputasi)
print('\nFilling the missing value (imputasi):')
print(retail_raw['quantity'].fillna(retail_raw.quantity.mean()))
# Drop missing value
print('\nDrop missing value:')
print(retail_raw['quantity'].dropna())

# nama_dataframe['nama_kolom'].fillna(nama_dataframe.nama_kolom.function())
#   .function() yang dimaksud pada syntax di atas adalah penggunan fungsi .mean() atau .mode().
#   Penggunaan fungsi .mean() atau .mode() ini bergantung pada kondisi yang mengharuskan menggunakan
#   nilai rata-rata atau modus dari kolom yang akan diimputasi.
