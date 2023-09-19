# =====  INSPEKSI  =====
import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datacovid19.csv')
# Cetak info dari df
print(df.info())
# Cetak jumlah missing value di setiap kolom
mv = df.isna().sum()
print('\nJumlah missing value per kolom:\n', mv)
# Method .isna() digunakan untuk mengecek berapa data yang bernilai NaN 
# dan .sum() menjumlahkannya secara default untuk masing-masing kolom dataframe.

# =====  TREATMENT  =====
import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak ukuran awal dataframe
print("Ukuran awal df: %d baris, %d kolom." % df.shape)
# Drop kolom yang seluruhnya missing value dan cetak ukurannya
df = df.dropna(axis=1, how='all')
print("Ukuran df setelah buang kolom dengan seluruh data missing: %d baris, %d kolom." % df.shape)
# Drop baris jika ada satu saja data yang missing dan cetak ukurannya
df = df.dropna(axis=0, how='any')
print("Ukuran df setelah dibuang baris yang memiliki sekurangnya 1 missing value: %d baris, %d kolom." % df.shape)
# method .dropna(): axis dan how. Keyword axis digunakan untuk menentukan arah dataframe yang akan dibuang angka 1 untuk menyatakan kolom (column-based)
#  Jika digunakan angka 0 berarti itu dalam searah index (row-based)
# Sementara, keyword how digunakan untuk bagaimana cara membuangnya. Opsi yang dapat diterimanya (dalam string) adalah
#  "all" artinya jika seluruh data di satu/beberapa kolom atau di satu/beberapa baris adalah missing value.
#  "any" artinya jika memiliki 1 saja data yang hilang maka buanglah baris/kolom tersebut.

# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak unique value pada kolom province_state
print("Unique value awal:\n", df['province_state'].unique())
# Ganti missing value dengan string "unknown_province_state"
df['province_state'] = df['province_state'].fillna('unknown_province_state')
# Cetak kembali unique value pada kolom province_state
print("Unique value setelah fillna:\n", df['province_state'].unique())

# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak nilai mean dan median awal 
print("Awal: mean = %f, median = %f." % (df["active"].mean(), df["active"].median()))
# Isi missing value kolom active dengan median
df_median = df["active"].fillna(df["active"].median())
# Cetak nilai mean dan median awal setelah diisi dengan median
print("Fillna median: mean = %f, median = %f." % (df_median.mean(), df_median.median()))
# Isi missing value kolom active dengan mean
df_mean = df["active"].fillna(df["active"].mean())
# Cetak nilai mean dan median awal setelah diisi dengan mean
print("Fillna mean: mean = %f, median = %f." % (df_mean.mean(), df_mean.median()))

import numpy as np
import pandas as pd
# Data
ts = pd.Series({
   "2020-01-01":9,
   "2020-01-02":np.nan,
   "2020-01-05":np.nan,
   "2020-01-07":24,
   "2020-01-10":np.nan,
   "2020-01-12":np.nan,
   "2020-01-15":33,
   "2020-01-17":np.nan,
   "2020-01-16":40,
   "2020-01-20":45,
   "2020-01-22":52,
   "2020-01-25":75,
   "2020-01-28":np.nan,
   "2020-01-30":np.nan
})
# Isi missing value menggunakan interpolasi linier
ts = ts.interpolate()
# Cetak time series setelah interpolasi linier
print("Setelah diisi missing valuenya:\n", ts)
