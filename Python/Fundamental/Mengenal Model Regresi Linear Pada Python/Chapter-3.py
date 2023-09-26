# =====  Menentukan Persamaan Linier  =====
import pandas as pd
df_kunjungan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/kunjungan_dokter_gigi_kota_x_dqlab.tsv", sep="\t")
df_penjualan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/tingkat_penjualan_kota_x_dqlab.tsv", sep="\t")
# Gabungkan kolom Tahun dan Bulan menjadi kolom Periode dengan isi tiap barisnya memiliki format YYYY-MM 
str_bulan = lambda x: "0"+str(x) if x<10 else str(x)
df_kunjungan["Periode"] = df_kunjungan["Tahun"].map(str) + "-" + df_kunjungan["Bulan"].map(str_bulan)
df_penjualan["Periode"] = df_penjualan["Tahun"].map(str) + "-" + df_penjualan["Bulan"].map(str_bulan)
# Drop kolom Tahun, Bulan dari df_kunjungan
df_kunjungan.drop(columns=["Tahun", "Bulan"], inplace=True)
# Drop kolom Tahun, Bulan dan No dari df_penjualan
df_penjualan.drop(columns=["Tahun", "Bulan", "No"], inplace=True)
# Set index kolom Periode
df_kunjungan.set_index("Periode", inplace=True)
df_penjualan.set_index("Periode", inplace=True)
# Gabungkan kedua dataframe dengan Periode yang telah menjadi key column nya
df = df_kunjungan.join(df_penjualan)
import numpy as np
# Ambillah variabel bebas dan bergantung df untuk keterlambatan 4 bulan
# dan ubahlah menjadi numpy 1d narray
x = df["penjualan permen"][:-4].to_numpy()
y = df["tingkat kunjungan ke dokter gigi"][4:].to_numpy()
# Hitunglah nilai rata-rata variabel bebas dan bergantung
x_mean = x.mean()
y_mean = y.mean()
# Hitung nilai pembilang dan penyebut untuk m
m_pembilang = ((x - x_mean) * (y - y_mean)).sum()
m_penyebut = ((x - x_mean)**2).sum()
# Hitung nilai koefisien regresi linier
m = m_pembilang / m_penyebut
b = y_mean - m * x_mean
print("Persamaan regresi linier: y = %.4e * x + %.4f" % (m, b))

# =====  Prediksi Tingkat Kunjungan  =====
import pandas as pd
import numpy as np
df_kunjungan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/kunjungan_dokter_gigi_kota_x_dqlab.tsv", sep="\t")
df_penjualan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/tingkat_penjualan_kota_x_dqlab.tsv", sep="\t")
# Gabungkan kolom Tahun dan Bulan menjadi kolom Periode dengan isi tiap barisnya memiliki format YYYY-MM 
str_bulan = lambda x: "0"+str(x) if x<10 else str(x)
df_kunjungan["Periode"] = df_kunjungan["Tahun"].map(str) + "-" + df_kunjungan["Bulan"].map(str_bulan)
df_penjualan["Periode"] = df_penjualan["Tahun"].map(str) + "-" + df_penjualan["Bulan"].map(str_bulan)
# Drop kolom Tahun, Bulan dari df_kunjungan
df_kunjungan.drop(columns=["Tahun", "Bulan"], inplace=True)
# Drop kolom Tahun, Bulan dan No dari df_penjualan
df_penjualan.drop(columns=["Tahun", "Bulan", "No"], inplace=True)
# Set index kolom Periode
df_kunjungan.set_index("Periode", inplace=True)
df_penjualan.set_index("Periode", inplace=True)
# Gabungkan kedua dataframe dengan Periode yang telah menjadi key column nya
df = df_kunjungan.join(df_penjualan)
# Ambillah variabel bebas dan bergantung df untuk keterlambatan 4 bulan
# dan ubahlah menjadi numpy 1d narray
x = df["penjualan permen"][:-4].to_numpy()
y = df["tingkat kunjungan ke dokter gigi"][4:].to_numpy()
# Hitunglah nilai rata-rata variabel bebas dan bergantung
x_mean = x.mean()
y_mean = y.mean()
# Hitung nilai pembilang dan penyebut untuk m
m_pembilang = ((x - x_mean) * (y - y_mean)).sum()
m_penyebut = ((x - x_mean)**2).sum()
# Hitung nilai koefisien regresi linier
m = m_pembilang / m_penyebut
b = y_mean - m * x_mean
# Ambillah butir data variabel bebas yang belum digunakan
x_new = df["penjualan permen"][-4:].to_numpy()
#  Gunakan x_new ke dalam persamaan regresi
y_pred = m * x_new + b
print("Prediksi tingkat kunjungan ke dokter gigi 1998-01 s/d 1998-04:")
for i, kunjungan in enumerate(y_pred):
    print("1998-0%d: %4d kunjungan." % (i+1, round(kunjungan)))

# =====  Regresi Linier dengan Scikit-Learn  =====
import pandas as pd
import numpy as np
df_kunjungan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/kunjungan_dokter_gigi_kota_x_dqlab.tsv", sep="\t")
df_penjualan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/tingkat_penjualan_kota_x_dqlab.tsv", sep="\t")
# Gabungkan kolom Tahun dan Bulan menjadi kolom Periode dengan isi tiap barisnya memiliki format YYYY-MM 
str_bulan = lambda x: "0"+str(x) if x<10 else str(x)
df_kunjungan["Periode"] = df_kunjungan["Tahun"].map(str) + "-" + df_kunjungan["Bulan"].map(str_bulan)
df_penjualan["Periode"] = df_penjualan["Tahun"].map(str) + "-" + df_penjualan["Bulan"].map(str_bulan)
# Drop kolom Tahun, Bulan dari df_kunjungan
df_kunjungan.drop(columns=["Tahun", "Bulan"], inplace=True)
# Drop kolom Tahun, Bulan dan No dari df_penjualan
df_penjualan.drop(columns=["Tahun", "Bulan", "No"], inplace=True)
# Set index kolom Periode
df_kunjungan.set_index("Periode", inplace=True)
df_penjualan.set_index("Periode", inplace=True)
# Gabungkan kedua dataframe dengan Periode yang telah menjadi key column nya
df = df_kunjungan.join(df_penjualan)
from sklearn.linear_model import LinearRegression
# Ambillah variabel bebas dan bergantung untuk keterlambatan 4 bulan
# dan ubahlah menjadi numpy 2d narray melalui .reshape((-1,1))
x = df["penjualan permen"][:-4].to_numpy().reshape((-1,1))
y = df["tingkat kunjungan ke dokter gigi"][4:].to_numpy().reshape((-1,1))
# Instansiasi LinearRegression ke dalam lr
lr = LinearRegression()
# Terapkan method fit pada variabel bebas dan bergantung
lr.fit(x,y)
# Ambillah butir data variabel bebas yang belum digunakan
# dan ubahlah menjadi numpy 2d narray melalui .reshape((-1,1))
x_new = df["penjualan permen"][-4:].to_numpy().reshape((-1,1))
# Prediksilah x_new dengan method predict
y_pred = lr.predict(x_new)
print("Persamaan regresi linier: y = %.4e * x + %.4f\n" % (lr.coef_, lr.intercept_))
print("Prediksi tingkat kunjungan ke dokter gigi 1998-01 s/d 1998-04:")
for i, kunjungan in enumerate(y_pred):
    print("1998-0%d: %4d kunjungan." % (i+1, round(kunjungan[0])))
