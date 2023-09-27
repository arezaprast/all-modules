# =====  Rata-rata (Mean)  =====
import numpy as np
import pandas as pd
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
#mengambil hanya data untuk produk 'A'
produk_A = raw_data[raw_data['Produk'] == 'A']
#menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame
print (produk_A['Pendapatan'].mean())
#menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame dengan numpy
print (np.mean(produk_A['Pendapatan']))

# =====  Median  =====
#Hitung median dari pendapatan menggunakan pandas
print(produk_A['Pendapatan'].median())
#Hitung median dari pendapatan menggunakan numpy
print(np.median(produk_A['Pendapatan']))

# =====  Modus  =====
#Melihat jumlah dari masing-masing produk
print(raw_data['Produk'].value_counts())

# =====  Kuantil  =====
#mencari median atau 50% dari data menggunakan pandas
print(raw_data['Pendapatan'].quantile(q=0.5))
#mencari median atau 50% dari data menggunakan numpy
print(np.quantile(raw_data['Pendapatan'], q=0.5))

# =====  Agregasi Data dengan method .agg()  =====
#menghitung rerata dan median 'Pendapatan' dan 'Harga'
print(raw_data[['Pendapatan', 'Harga']].agg([np.mean, np.median]))
#menghitung rerata dan median Pendapatan dan Harga dari tiap produk
print(raw_data[['Pendapatan', 'Harga', 'Produk']].groupby('Produk').agg([np.mean, np.median]))
