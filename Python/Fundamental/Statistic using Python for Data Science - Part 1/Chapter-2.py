# =====  Load Library  =====
import numpy as np
import pandas as pd

# =====  Load Dataset  =====
import pandas as pd
# memuat data bernama 'dataset_statistics.csv' dan memasukkan hasilnya ke dalam 'raw_data'
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# =====  Inspeksi Data  =====
#melihat 10 data pada baris pertama
print (raw_data.head(10))
#melihat 5 data pada baris terakhir
print (raw_data.tail())

# =====  Metode Shape  =====
# melihat dimensi dari raw_data
print (raw_data.shape)
# mengambil jumlah data
print (raw_data.shape[0])

# =====  Melihat Kolom Dalam Dataset  =====
print(raw_data.columns)

# =====  Metode Isna  =====
print (raw_data.isna())
print (raw_data.isna().sum())

# =====  Metode Describe  =====
print (raw_data.describe())
#Mencari nilai maksimum dari tiap kolom
raw_data.max()
#Mencari nilai maksimum dari kolom 'Harga'
raw_data['Harga'].max()
#Mencari nilai minimum dari kolom 'Harga'
raw_data['Harga'].min()

# =====  Metode Sum  =====
#menghitung jumlah dari semua kolom
print (raw_data.sum())
#menghitung jumlah dari semua kolom bertipe data numerik saja
raw_data.sum(numeric_only=True)
#menghitung jumlah dari kolom 'Harga' dan 'Pendapatan'
raw_data[['Harga', 'Pendapatan']].sum()

# =====  Manipulasi Dataframe - Memilih Kolom dan Baris  =====
#Memilih kolom 'Pendapatan' saja
print(raw_data['Pendapatan'])
#Memilih kolom 'Jenis Kelamin' dan 'Pendapatan'
print(raw_data[['Jenis Kelamin', 'Pendapatan']])

# =====  Metode Loc  =====
#mengambil data dari baris ke-0 sampai baris ke-(10-1) atau baris ke-9
print (raw_data[:10])
#mengambil data dari baris ke-3 sampai baris ke-(5-1) atau baris ke-4
print (raw_data[3:5])
# mengambil data pada baris ke-1, ke-3 dan ke-10
print (raw_data.loc[[1,3,10]])
#Mengambil kolom 'Jenis Kelamin' dan 'Pendapatan' dan ambil baris ke-1 sampai ke-9
print (raw_data[['Jenis Kelamin', 'Pendapatan']][1:10])
#Mengambil kolom 'Harga' dan 'Tingkat Kepuasan' dan ambil baris ke-1, ke-10 dan ke-15
print (raw_data[['Harga', 'Tingkat Kepuasan']].loc[[1,10,15]])
