# =====  Task 1 - Library Import and File Unloading  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
#lakukan pembacaan dataset
movie_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.basics.tsv', sep='/t') #untuk menyimpan title_basics.tsv
rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.ratings.tsv', sep='/t') #untuk menyimpan title.ratings.tsv

# =====  Task 2 - Cleaning table movie  =====
# 5 Data teratas dari table movie
print(movie_df.head())
# Info Data dari Setiap Kolom
print(movie_df.info())
# Pengecekan Data dengan Nilai NULL
print(movie_df.isnull().sum())
# Analisis Kolom dengan data bernilai NULL - part 1
print(movie_df.loc[(movie_df['primaryTitle'].isnull()) | (movie_df['originalTitle'].isnull())])
# Membuang Data dengan Nilai NULL - part 1
#mengupdate movie_df dengan membuang data-data bernilai NULL
movie_df = movie_df.loc[(movie_df['primaryTitle'].notnull()) & (movie_df['originalTitle'].notnull())]
#menampilkan jumlah data setelah data dengan nilai NULL dibuang
print(len(movie_df))
# Analisis Kolom dengan data bernilai NULL - part 2
print(movie_df.loc[(movie_df['genres'].isnull())])
# Membuang Data dengan Nilai NULL - part 2
#mengupdate movie_df dengan membuang data-data bernilai NULL
movie_df = movie_df.loc[(movie_df['genres'].notnull())]
#menampilkan jumlah data setelah data dengan nilai NULL dibuang
print(len(movie_df))
# Mengubah Nilai '\\N'
#mengubah nilai '\\N' pada startYear menjadi np.nan dan cast kolomnya menjadi float64
movie_df['startYear'] = movie_df['startYear'].replace('\\N',np.nan)
movie_df['startYear'] = movie_df['startYear'].astype('float64')
print(movie_df['startYear'].unique()[:5])
#mengubah nilai '\\N' pada endYear menjadi np.nan dan cast kolomnya menjadi float64
movie_df['endYear'] = movie_df['endYear'].replace('\\N',np.nan)
movie_df['endYear'] = movie_df['endYear'].astype('float64')
print(movie_df['endYear'].unique()[:5])
#mengubah nilai '\\N' pada runtimeMinutes menjadi np.nan dan cast kolomnya menjadi float64
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].replace('\\N',np.nan)
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].astype('float64')
print(movie_df['runtimeMinutes'].unique()[:5])
# Mengubah nilai genres menjadi list
def transform_to_list(x):
    if ',' in x: 
    #ubah menjadi list apabila ada data pada kolom genre
        return x.split(',')
    else: 
    #jika tidak ada data, ubah menjadi list kosong
        return []
movie_df['genres'] = movie_df['genres'].apply(lambda x: transform_to_list(x))

