# Membaca Dataset
import pandas as pd
# Baca dataset kunjungan_dokter_gigi_kota_x_dqlab.tsv sesuai dengan url yang diberikan
df_kunjungan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/kunjungan_dokter_gigi_kota_x_dqlab.tsv", sep='\t')
# Cetak ukuran dataset sehingga diketahui jumlah baris dan kolomnya
print("Ukuran df_kunjungan:", df_kunjungan.shape)
# Cetak data frame df_kunjungan
print(df_kunjungan)
# Baca dataset tingkat_penjualan_kota_x_dqlab.tsv sesuai dengan url yang diberikan
df_penjualan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/tingkat_penjualan_kota_x_dqlab.tsv", sep='\t')
# Cetak ukuran dataset sehingga diketahui jumlah baris dan kolomnya
print("\n\nUkuran df_penjualan:", df_penjualan.shape)
# Cetak data frame df_penjualan
print(df_penjualan)

# Penggabungan Kolom Tahun dan Bulan
import pandas as pd
# Baca kedua dataset
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
# Inspeksi nama-nama kolom di kedua dataframe
print("Nama kolom df_kunjungan:", df_kunjungan.columns)
print("\nNama kolom df_penjualan", df_penjualan.columns)

# Penggabungan Kedua Dataset
import pandas as pd
pd.set_option("display.max_columns",5)
# Baca kedua dataset
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
print("Ukuran df:", df.shape)
print(df)

# Korelasi Penjualan Makanan dengan Kunjungan ke Dokter Gigi: Visualisasi
import pandas as pd
# Baca kedua dataset
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
import matplotlib.pyplot as plt
# Kolom x adalah kolom dengan awalan penjualan
x_cols = df.columns[1:]
# Kolom y merupakan kolom tingkat kunjungan ke dokter gigi
y_col = "tingkat kunjungan ke dokter gigi"
# Buat visualisasi 
fig, axs = plt.subplots(len(x_cols), 1, figsize=(8,12))
for ax, x_col in zip(axs, x_cols):
    # Plotkan dengan scatter
    df.plot.scatter(x=x_col, y=y_col, c="darkcyan", s=60, ax=ax)
    ax.set_xlabel(x_col, fontsize=14)
    ax.set_ylabel(y_col, fontsize=14)
    ax.grid()
plt.tight_layout()
plt.show()

# Korelasi Penjualan Makanan dengan Kunjungan ke Dokter Gigi: Koefisien Korelasi Pearson
import pandas as pd
# Baca kedua dataset
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
print("Koefisien korelasi Pearson:")
print("---------------------------")
print(df.corr()["tingkat kunjungan ke dokter gigi"])

# The Delayed Effect
import pandas as pd
# Baca kedua dataset
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
import matplotlib.pyplot as plt
from scipy import stats
# Spesifikasi keterlambatan hingga 8 bulan
n_delays = 8 
# Spesifikasi jumlah kolom untuk subplots
n_plt_cols = 2
fig, axs = plt.subplots(round(n_delays/2), n_plt_cols, figsize=(12, 3.5*round(n_delays/2)), sharey=True)
for i in range(n_delays):
    # Ingat: varibel bebas dan variabel bergantung harus memiliki ukuran yang sama
    # Ambilah variabel bebas: penjualan permen
    x = df["penjualan permen"][:-(i+1)]
    # Ambilah variabel bergantung: tingkat kunjungan ke dokter gigi dan implementasikan keterlambatan
    y = df["tingkat kunjungan ke dokter gigi"][i+1:]
    # Hitung koefisien korelasi Pearson
    pearson_r, p_value = stats.pearsonr(x, y)
    # Buat title setiap subplots dan juga tambatkan nilai  
    # koefisien korelasi Pearson yang telah dihitung
    title = "Efek keterlambatan %d bulan (r = %.2f)" % (i+1, pearson_r)
    # Buat scatter plot
    ax = axs[i // n_plt_cols][i % n_plt_cols]
    ax.scatter(x, y, c="darkcyan")
    ax.set_title(title, fontsize=14, color="maroon")
    if i % n_plt_cols == 0:
        ax.set_ylabel("tingkat kunjungan ke dokter gigi", fontsize=12)
    ax.set_xlabel("penjualan permen", fontsize=12)
    ax.set_xlim([120000, 480000])
    ax.grid()
plt.tight_layout()
plt.show()
