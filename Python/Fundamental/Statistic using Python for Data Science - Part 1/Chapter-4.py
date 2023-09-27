# =====  Proporsi Kategori  =====
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
#cari proporsi tiap Produk
print(raw_data['Produk'].value_counts()/raw_data.shape[0])

# =====  Ukuran Sebaran pada Data Interval dan Rasio  =====
# Cari nilai rentang dari kolom 'Pendapatan'
print (raw_data['Pendapatan'].max() - raw_data['Pendapatan'].min())

# =====  Variansi  =====
#menghitung variansi Pendapatan menggunakan method .var() dari pandas
print (raw_data['Pendapatan'].var())
#menghitung variansi Pendapatan menggunakan method .var() dari numpy
print (np.var(raw_data['Pendapatan']))
#mengatur variansi populasi dengan method `.var()` dari pandas
print (raw_data['Pendapatan'].var(ddof=0))

# =====  Deviasi Baku (Standard Deviation)  =====
#menghitung deviasi baku sampel pendapatan menggunakan method std() dari pandas
print(raw_data['Pendapatan'].std())
#menghitung deviasi baku sampel pendapatan menggunakan method std() dari numpy
print (np.std(raw_data['Pendapatan'], ddof=1))
