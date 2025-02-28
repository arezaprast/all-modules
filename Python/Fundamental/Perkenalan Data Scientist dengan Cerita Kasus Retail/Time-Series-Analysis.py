#--- Membaca Dataset ---
#Mengimpor library pandas
import pandas as pd
pd.set_option('display.max_column', 20)
#Membaca file
dataset_retail = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/data_retail.csv', delimiter=';')
#Menampilkan isi data
print(dataset_retail)

#--- Melihat Detail dari Dataset ---
#Kode sebelumnya
#Melihat detail tipe data
dataset_retail.info()

#--- Mengubah Format Tanggal ---
#Kode sebelumnya
#Mengimpor library datetime
import datetime
#Mengubah kolom first_Transaction dan Last_Transaction ke bentuk Datetime
dataset_retail['First_Transaction']= pd.to_datetime(pd.to_datetime(dataset_retail['First_Transaction']/1000, unit='s', origin='1970-01-01')).dt.date
dataset_retail['Last_Transaction']= pd.to_datetime(pd.to_datetime(dataset_retail['Last_Transaction']/1000, unit='s', origin='1970-01-01')).dt.date
dataset_retail.sort_values('First_Transaction', inplace=True)
#Menampilkan isi data
print(dataset_retail)

#--- Melihat Pola Transaksi dari Waktu ke Waktu ---
#Kode sebelumnya
#Kita akan buat agregasi rata-rata jumlah transaksi harian berdasarkan kolom First_Transaction
daily_avg_trx = dataset_retail.groupby('First_Transaction').mean()['Average_Transaction_Amount'].reset_index()
#Mengimport library matplotlib
import matplotlib.pyplot as plt
#Menampilkan nilai rata-rata jumlah transaksi dalam bentuk grafik
plt.plot(daily_avg_trx['First_Transaction'],daily_avg_trx['Average_Transaction_Amount'])
plt.xlabel('Transaksi Pertama')
plt.ylabel('Rata-rata jumlah transaksi')
plt.grid()
plt.show()

#--- Melakukan Pengecekan Kestasioneran Data ---
#Kode sebelumnya
#Mengimpor library adfuller
from statsmodels.tsa.stattools import adfuller
#Mengecek stationary data
df_stationarityTest = adfuller(daily_avg_trx['Average_Transaction_Amount'])
print("p-value: ", df_stationarityTest[1])

#--- Menggunakan Plot untuk Mengetahui Order Terbaik ---
#Kode sebelumnya
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 1, figsize=(8,8))
#Menampilkan Autocorrelation Plots
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(daily_avg_trx['Average_Transaction_Amount'], ax=axs[0])
#Menampilkan Partial Autocorrelation Plots
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(daily_avg_trx['Average_Transaction_Amount'], ax=axs[1])
plt.tight_layout()
plt.show()

#--- Menampilkan Plot PACF untuk lags dari 1 hingga 20 ---
#Kode sebelumnya
import matplotlib.pyplot as plt
fig, axs = plt.subplots(20, 1, figsize=(8,50))
#Menampilkan Partial Autocorrelation Plots
from statsmodels.graphics.tsaplots import plot_pacf
#Plot dengan lags 1 hingga 20
for i, ax in enumerate(axs):
	plot_pacf(daily_avg_trx['Average_Transaction_Amount'], lags=i+1, ax=ax)
	ax.set_title('Partial Autocorrelation with lag = %d' % (i+1,))
plt.tight_layout()
plt.show()

#--- Pemodelan dengan AutoRegression ---
#Kode sebelumnya
#Pembagian dataset atas training dan testing
train_data = daily_avg_trx['Average_Transaction_Amount'][:len(daily_avg_trx)-10]
test_data = daily_avg_trx['Average_Transaction_Amount'][len(daily_avg_trx)-10:]
print('Ukuran data training:', train_data.shape)
print('Ukuran data testing :', test_data.shape)
#Model auto regression
from statsmodels.tsa.ar_model import AutoReg
#Fit data ke dalam mode
ar_model = AutoReg(train_data, lags=10).fit()
print(ar_model.summary())

#--- Menguji Model Dengan Membuat Prediksi ---
#Kode Sebelumnya
#Membuat prediksi dengan model
pred = ar_model.predict(start=len(train_data), end=(len(train_data)+len(test_data)-1), dynamic=False).rename('AR Predictions')
#Plot
import matplotlib.pyplot as plt
pred.plot(legend=True)
test_data.plot(legend=True)
plt.xlabel('Urutan data First_Transaction ke-')
plt.tight_layout()
plt.show()
