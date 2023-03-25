import pandas as pd
# Series
number_list = pd.Series([1,2,3,4,5,6])
# DataFrame
matrix_list = pd.DataFrame([[1,2,3],
			    ['a','b','c'],
			    [3,4,5],
			    ['d',4,6]])
# [1] method .info()
#   digunakan untuk mengecek kolom apa yang membentuk dataframe itu, data types, berapa yang non null, dll.
#   Method ini tidak dapat digunakan pada series, hanya pada dataframe saja.
print("[1] method .info()")
print(matrix_list.info())
# [2] attribute .shape
#   digunakan untuk mengetahui berapa baris dan kolom, hasilnya dalam format tuple (baris, kolom).
print("\n[2] attribute .shape")
print("    Shape dari number_list:", number_list.shape)
print("    Shape dari matrix_list:", matrix_list.shape)
# [3] attribute .dtypes
#   digunakan untuk mengetahui tipe data di tiap kolom. Tipe data object: kombinasi-
#   untuk berbagai tipe data (number & text, etc).
print("\n[3] attribute .dtypes")
print("    Tipe data number_list:", number_list.dtypes)
print("    Tipe data matrix_list:", matrix_list.dtypes)
# [4] attribute .astype()
#   untuk convert tipe data berdasarkan tipe data seperti:
#   float, int, str, numpy.float, numpy.int ataupun numpy.datetime.
print("\n[4] method .astype()")
print("    Konversi number_list ke str:", number_list.astype(str))
print("    Konversi matrix_list ke str:", matrix_list.astype(str))
