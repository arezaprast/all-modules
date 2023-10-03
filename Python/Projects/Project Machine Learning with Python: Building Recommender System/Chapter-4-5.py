# [Chapter - 4]
# =====  Menampilkan 5 data teratas  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.ratings.tsv', sep='\t')
print(rating_df.head())
# =====  Menampilkan info data  =====
print(rating_df.info())

# [Chapter - 5]
# =====  Inner Join table movie dan table rating  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
movie_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.basics.tsv', sep='\t')
rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.ratings.tsv', sep='\t')
movie_df = movie_df.loc[(movie_df['primaryTitle'].notnull()) & (movie_df['originalTitle'].notnull())]
movie_df = movie_df.loc[movie_df['genres'].notnull()]
movie_df['startYear'] = movie_df['startYear'].replace('\\N', np.nan)
movie_df['startYear'] = movie_df['startYear'].astype('float64')
movie_df['endYear'] = movie_df['endYear'].replace('\\N', np.nan)
movie_df['endYear'] = movie_df['endYear'].astype('float64')
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].replace('\\N', np.nan)
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].astype('float64')
def transform_to_list(x):
    if ',' in x: 
        return x.split(',')
    else: 
        return []
movie_df['genres'] = movie_df['genres'].apply(lambda x: transform_to_list(x))
#Lakukan join pada kedua table
movie_rating_df = pd.merge(movie_df, rating_df, on='tconst', how='inner')
#Tampilkan 5 data teratas
print(movie_rating_df.head())
#Tampilkan tipe data dari tiap kolom
print(movie_rating_df.info())
# =====  Memperkecil ukuran Table  =====
movie_df['genres'] = movie_df['genres'].apply(lambda x: transform_to_list(x))
movie_rating_df = pd.merge(movie_df, rating_df, on='tconst', how='inner')
movie_rating_df = movie_rating_df.dropna(subset=['startYear', 'runtimeMinutes'])
#Untuk memastikan bahwa sudah tidak ada lagi nilai NULL
print(movie_rating_df.info())
