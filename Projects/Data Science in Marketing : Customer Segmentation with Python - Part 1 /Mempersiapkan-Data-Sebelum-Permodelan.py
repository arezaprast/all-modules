# Standarisasi Kolom Numerik
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/customer_segments.txt", sep="\t")
from sklearn.preprocessing import StandardScaler  
kolom_numerik  = ['Umur','NilaiBelanjaSetahun']  
# Statistik sebelum Standardisasi  
print('Statistik Sebelum Standardisasi\n')  
print(df[kolom_numerik ].describe().round(1))  
# Standardisasi  
df_std = StandardScaler().fit_transform(df[kolom_numerik])  
# Membuat DataFrame  
df_std = pd.DataFrame(data=df_std, index=df.index, columns=df[kolom_numerik].columns)  
# Menampilkan contoh isi data dan summary statistic  
print('Contoh hasil standardisasi\n')  
print(df_std.head())  
print('Statistik hasil standardisasi\n')  
print(df_std.describe().round(0)) 

# Konversi Kategorikal Data dengan Label Encoder
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/customer_segments.txt", sep="\t")
from sklearn.preprocessing import LabelEncoder  
# Inisiasi nama kolom kategorikal  
kolom_kategorikal = ['Jenis Kelamin','Profesi','Tipe Residen']  
# Membuat salinan data frame  
df_encode = df[kolom_kategorikal].copy()  
# Melakukan labelEncoder untuk semua kolom kategorikal  
for col in kolom_kategorikal:  
    df_encode[col] = LabelEncoder().fit_transform(df_encode[col])  
# Menampilkan data  
print(df_encode.head())

# Menggabungkan Data untuk Permodelan
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/customer_segments.txt", sep="\t")
kolom_numerik  = ['Umur','NilaiBelanjaSetahun']
df_std = StandardScaler().fit_transform(df[kolom_numerik])
df_std = pd.DataFrame(data=df_std, index=df.index, columns=df[kolom_numerik].columns)
kolom_kategorikal = ['Jenis Kelamin','Profesi','Tipe Residen']
df_encode = df[kolom_kategorikal].copy()
for col in kolom_kategorikal:
    df_encode[col] = LabelEncoder().fit_transform(df_encode[col])
# Menggabungkan data frame
df_model= df_encode.merge(df_std, left_index=True, right_index=True, how= 'left')  
print(df_model.head())
