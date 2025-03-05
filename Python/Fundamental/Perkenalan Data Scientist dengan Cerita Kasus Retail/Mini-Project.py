#membaca file dengan pandas
import pandas as pd
#gunakan function yang digunakan sama dengan membaca file csv
dataset_transaksi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/transaksi_dqlab_retail.tsv', sep='\t')
dataset_transaksi['Flag'] = 1
#kelompokkan Kode Transaksi dan Nama Barang dengan menjumlahkan Flag
basket = dataset_transaksi.groupby(['Kode Transaksi','Nama Barang'])['Flag'].sum().unstack().reset_index().fillna(0).set_index('Kode Transaksi')
#Membuat function untuk menormalisasi data
def encode_units(x):
	if x <= 0:
		return 0
	if x > 0:
		return 1
#menerapkan fungsi yang telah dibuat untuk menormalisasi data
basket_encode = basket.applymap(encode_units)
from mlxtend.frequent_patterns import apriori
#menerapkan algoritma untuk apriori parameter untuk menentukan nilai minimal dari Support
frequent_itemset = apriori(basket_encode, min_support=0.04, use_colnames=True)
print(frequent_itemset)
from mlxtend.frequent_patterns import association_rules
#menerapkan aturan untuk mencari asosiasi antar produk gunakan dataset yang telah diterapkan apriori diurutkan berdasarkan metrik yang digunakan
rules = association_rules(frequent_itemset, metric='lift', min_threshold=1).sort_values('lift', ascending=False).reset_index(drop=True)
print(rules)
