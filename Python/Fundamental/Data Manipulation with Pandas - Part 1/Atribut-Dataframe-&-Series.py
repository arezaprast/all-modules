import pandas as pd
number_list = pd.Series([1,2,3,4,5,6]) # Series
matrix_list = pd.DataFrame([[1,2,3],
                            ['a','b','c'],
                            [3,4,5],
                            ['d',4,6]]) # DataFrame
# [1] method .info()
# digunakan untuk mengecek kolom apa yang membentuk dataframe itu, data types, berapa yang non null, dll.
# Method ini tidak dapat digunakan pada series, hanya pada dataframe saja.
print("[1] method .info()")
print(matrix_list.info())
# [2] attribute .shape
# digunakan untuk mengetahui berapa baris dan kolom, hasilnya dalam format tuple (baris, kolom).
print("\n[2] attribute .shape")
print("    Shape dari number_list:", number_list.shape)
print("    Shape dari matrix_list:", matrix_list.shape)
# [3] attribute .dtypes
# digunakan untuk mengetahui tipe data di tiap kolom. Tipe data object: kombinasi-
# untuk berbagai tipe data (number & text, etc).
print("\n[3] attribute .dtypes")
print("    Tipe data number_list:", number_list.dtypes)
print("    Tipe data matrix_list:", matrix_list.dtypes)
# [4] attribute .astype()
# untuk convert tipe data berdasarkan tipe data seperti:
# float, int, str, numpy.float, numpy.int ataupun numpy.datetime.
print("\n[4] method .astype()")
print("    Konversi number_list ke str:", number_list.astype(str))
print("    Konversi matrix_list ke str:", matrix_list.astype(str))
# [5] attribute .copy()
# digunakan melakukan duplikat, untuk disimpan di variable yang berbeda- 
# mungkin supaya tidak loading data lagi.
print("[5] attribute .copy()")
num_list = number_list.copy()
print("    Copy number_list ke num_list:", num_list)
mtr_list = matrix_list.copy()
print("    Copy matrix_list ke mtr_list:", mtr_list)	
# [6] attribute .to_list()
# digunakan untuk mengubah series menjadi list dan tidak dapat digunakan untuk dataframe.
print("[6] attribute .to_list()")
print(number_list.to_list())
# [7] attribute .unique()
# digunakan menghasilkan nilai unik dari suatu kolom, hasilnya dalam bentuk numpy array.
# Attribute ini hanya digunakan pada series saja.
print("[7] attribute .unique()")
print(number_list.unique())
# [8] attribute .index
# digunakan untuk mencari index/key dari Series atau Dataframe.
print("[8] attribute .index")
print("    Index number_list:", number_list.index)
print("    Index matrix_list:", matrix_list.index)	
# [9] attribute .columns
# digunakan untuk mengetahui apa saja kolom yang tersedia di dataframe-
# tersebut (hanya digunakan untuk dataframe saja). 
print("[9] attribute .columns")
print("    Column matrix_list:", matrix_list.columns)
# [10] attribute .loc
# digunakan slice dataframe atau series berdasarkan nama kolom dan/atau nama index.
print("[10] attribute .loc")
print("    .loc[0:1] pada number_list:", number_list.loc[0:1])
print("    .loc[0:1] pada matrix_list:", matrix_list.loc[0:1])
# [11] attribute .iloc
# digunakan untuk slice dataframe atau series berdasarkan index kolom dan/atau index.
print("[11] attribute .iloc")
print("    iloc[0:1] pada number_list:", number_list.iloc[0:1])
print("    iloc[0:1] pada matrix_list:", matrix_list.iloc[0:1])
