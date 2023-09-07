# Membaca Data Survei
import pandas as pd
# Membaca file survei_tinggi_badan.txt
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
# Mencetak 5 data teratas
print(df.head(5))

# Mengubah Nama Kolom
import pandas as pd
# membaca file survei_tinggi_badan.txt
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
# melakukan rename terhadap kolom "tinggi badan (cm)" menjadi "tinggi"
df.rename({'tinggi badan (cm)' : 'tinggi'}, axis=1, inplace=True)
print(df.head(5))

# Nilai Mean
import pandas as pd
# membaca file survei_tinggi_badan.txt
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
# melakukan rename terhadap kolom "tinggi badan (cm)" menjadi "tinggi"
df.rename({'tinggi badan (cm)' : 'tinggi'}, axis=1, inplace=True)
# Mengecek apakah ada data yang bernilai null
print("Mengecek apakah ada data yang bernilai null")
print(df.isnull().any().any())
# Mengecek jumlah data
print("\nMengecek jumlah data")
print(df.shape)
# Mendapatkan nilai mean menggunakan fungsi mean yang disediakan pandas
print("\nMean:", df['tinggi'].mean())

# Nilai Median dan Modus
import pandas as pd
# Membaca file survei_tinggi_badan.txt
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
# melakukan rename terhadap kolom "tinggi badan (cm)" menjadi "tinggi"
df.rename({'tinggi badan (cm)' : 'tinggi'}, axis=1, inplace=True)
# Mendapatkan nilai median menggunakan fungsi median yang disediakan pandas
print("Median data")
print('>> Median: ', df['tinggi'].median())
# Mendapatkan nilai modus menggunakan fungsi mode yang disediakan pandas
print("\nModus data")
print('>> Modus: ', df['tinggi'].mode())
