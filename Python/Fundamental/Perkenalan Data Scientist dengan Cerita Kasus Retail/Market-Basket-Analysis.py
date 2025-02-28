#--- Membaca Data Transaksi ---
#Mengimpor library pandas & numpy
import pandas as pd
import numpy as np
#Membaca file
dataset_transaksi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/transaksi_dqlab_retail.tsv', sep='\t')
#Menampilkan isi data
print(dataset_transaksi)

#--- Melihat Detail dari Dataset ---
#Kode sebelumnya
#Melihat detail tipe data
dataset_transaksi.info()

#--- Membuat Flag ---
#Kode sebelumnya
#Flag digunakan untuk menandakan barang/item terdapat pada basket.
dataset_transaksi['Flag'] = 1
#Menampilkan isi data
print(dataset_transaksi)

#--- Mengelompokkan 'Flag' Berdasarkan 'Kode Transaksi' dan 'Nama Barang' ---
#Kode sebelumnya
#Melakukan pengelompokkan Flag berdasarkan kolom Kode Transaksi dan Nama Barang
basket = dataset_transaksi.groupby(['Kode Transaksi','Nama Barang'])['Flag'].sum().unstack().reset_index().fillna(0).set_index('Kode Transaksi')
#Menampilkan basket
print(basket)

#--- Normalisasi Data ---
#Kode sebelumnya
#Membuat function untuk menormalisasi data
def encode_units(x):
	if x <= 0 :
		return 0
	if x > 0:
		return 1
#Menerapkan fungsi encode_units pada dataset	
basket_encode = basket.applymap(encode_units)
#Menampilkan basket_encode
print(basket_encode)

#--- Menggunakan Algoritma Apriori dengan Python 1 ---
#Kode sebelumnya
#Mengimport algoritma apriori
from mlxtend.frequent_patterns import apriori
#Menerapkan algoritma apriori untuk mendapatkan frequent_itemset
frequent_itemset = apriori(basket_encode, min_support=0.03, use_colnames=True)
print(frequent_itemset)

#--- Menggunakan Algoritma Apriori dengan Python 2 ---
#Kode sebelumnya
#Mengimport association_rules
from mlxtend.frequent_patterns import association_rules
#Menerapkan association_rules berdasarkan frequent_itemset
rules = association_rules(frequent_itemset, metric='lift', min_threshold=1).sort_values('lift', ascending=False).reset_index(drop=True)
print(rules)
