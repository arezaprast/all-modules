# [Chapter - 2]
# =====  Import Basics Library and File Unloading  =====
import pandas as pd
import numpy as np
movie_rating_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/movie_rating_df.csv ") #untuk menyimpan movie_rating_df.csv
# =====  Menampilkan 5 data teratas dan info data  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
movie_rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/movie_rating_df.csv')
#tampilkan 5 baris teratas dari movive_rating_df
print(movie_rating_df.head())
#tampilkan info mengenai tipe data dari tiap kolom
print(movie_rating_df.info())
# =====  Convert into List  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
director_writers = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/directors_writers.csv')
#Mengubah director_name menjadi list
director_writers['director_name'] = director_writers['director_name'].apply(lambda row: row.split(','))
director_writers['writer_name'] = director_writers['writer_name'].apply(lambda row: row.split(','))
#Tampilkan 5 data teratas
print(director_writers.head())

# [Chapter - 3]
# =====  Update name_df  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
name_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/actor_name.csv')
#Kita hanya akan membutuhkan kolom nconst, primaryName, dan knownForTitles
name_df = name_df[['nconst','primaryName','knownForTitles']]
#Tampilkan 5 baris teratas dari name_df
print(name_df.head())
# =====  Movies per Actor  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
name_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/actor_name.csv')
name_df = name_df[['nconst','primaryName','knownForTitles']]
#Melakukan pengecekan variasi
print(name_df['knownForTitles'].apply(lambda x: len(x.split(','))).unique)
#Mengubah knownForTitles menjadi list of list
name_df['knownForTitles'] = name_df['knownForTitles'].apply(lambda x: x.split(','))
#Mencetak 5 baris teratas
print(name_df.head())
# =====  Korespondensi 1 - 1  =====
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
name_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/actor_name.csv')
name_df = name_df[['nconst','primaryName','knownForTitles']]
name_df['knownForTitles'] = name_df['knownForTitles'].apply(lambda x: x.split(','))
#menyiapkan bucket untuk dataframe
df_uni = []
for x in ['knownForTitles']:
    #mengulang index dari tiap baris sampai tiap elemen dari knownForTitles
    idx = name_df.index.repeat(name_df['knownForTitles'].str.len())
   #memecah values dari list di setiap baris dan menggabungkan nya dengan rows lain menjadi dataframe
    df1 = pd.DataFrame({
        x: np.concatenate(name_df[x].values)
    })
    #mengganti index dataframe tersebut dengan idx yang sudah kita define di awal
    df1.index = idx
    #untuk setiap dataframe yang terbentuk, kita append ke dataframe bucket
    df_uni.append(df1)
#menggabungkan semua dataframe menjadi satu
df_concat = pd.concat(df_uni, axis=1)
#left join dengan value dari dataframe yang awal
unnested_df = df_concat.join(name_df.drop(['knownForTitles'], 1), how='left')
#select kolom sesuai dengan dataframe awal
unnested_df = unnested_df[name_df.columns.tolist()]
print(unnested_df)
