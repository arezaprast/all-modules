# [Chapter - 1]
# =====  Implementasi Visualisasi Data Statistik  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter='\t')
print(df.head(5))
# =====  Mengelompokkan Data  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
# menghitung total jumlah barang yang dibeli berdasarkan produk
print(df['Jumlah'].groupby(df['Nama Produk']).sum())
# =====  Mengubah Tanggal  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
import datetime
#membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"
df['Bulan'] = df['Tanggal'].apply(
	lambda x: datetime.datetime.strptime(x, '%d-%m-%Y').strftime('%m-%Y')
)
#menghitung jumlah item penjualan per produk per bulan
print(df.groupby(['Bulan', 'Nama Produk'])['Jumlah'].sum)
# =====  Grafik Scatter Plot  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
import datetime
#membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"
df["Bulan"] = df["Tanggal"].apply(
	lambda x: datetime.datetime.strptime(x, "%d-%m-%Y").strftime("%m-%Y")
)
import matplotlib.pyplot as plt
#plot scatter untuk kolom "Harga" dan "Jumlah"
plt.scatter(df["Harga"], df["Jumlah"], alpha = 0.2)
plt.xlabel("Harga", fontsize=11)
plt.ylabel("Jumlah", fontsize=11)
plt.tight_layout()
plt.show()
# =====  Grafik Histogram  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
import datetime
#membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"
df["Bulan"] = df["Tanggal"].apply(
	lambda x: datetime.datetime.strptime(x, "%d-%m-%Y").strftime("%m-%Y")
)
#menampilkan histogram jumlah
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.hist(df["Jumlah"])
plt.grid(color="gray", linestyle="-", linewidth=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# =====  Line Chart  =====
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
import datetime
#membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"
df["Bulan"] = df["Tanggal"].apply(
	lambda x: datetime.datetime.strptime(x, "%d-%m-%Y").strftime("%m-%Y")
)
#mengambil data Mi Goreng Instant saja
produk_mi = df[df['Nama Produk'] == 'Mi Goreng Instant']
#x adalah bulan transaksi
x = ['04-2020','05-2020','06-2020']
#y jumlah item Mi Goreng Instant yang terjual
y = produk_mi.groupby(["Bulan","Nama Produk"])['Jumlah'].sum()
#membuat line chart menggunakan fungsi plot
plt.plot(x,y)
plt.title('Jumlah Penjualan Mi Goreng Instant Per Bulan', pad=10, fontsize=12, color='blue')
plt.xlabel('Bulan', fontsize=11)
plt.ylabel('Jumlah', fontsize=11)
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.show()

# [Mini Project]
# =====  Membuat Tabel Frekuensi  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
import datetime
#membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"
df["Bulan"] = df["Tanggal"].apply(
	lambda x: datetime.datetime.strptime(x, "%d-%m-%Y").strftime("%m-%Y")
)
#Menghitung total harga untuk setiap row
df["Total"] = df["Harga"] * df["Jumlah"]
#menghitung total penjualan per produk per bulan
print(df.groupby(["Bulan", "Nama Produk"])["Total"].sum())
# =====  Membuat Line Chart  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
import datetime
#membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"
df["Bulan"] = df["Tanggal"].apply(
	lambda x: datetime.datetime.strptime(x, "%d-%m-%Y").strftime("%m-%Y")
)
#mengambil data Kopi Instant saja
produk_kopi = df[df["Nama Produk"] == "Kopi Instant"]
#x adalah bulan transaksi
x = ["04-2020", "05-2020", "06-2020"]
#y jumlah item Kopi Instant yang terjual
y = produk_kopi.groupby(["Bulan", "Nama Produk"])["Jumlah"].sum()
import matplotlib.pyplot as plt
#membuat line chart menggunakan fungsi plot
plt.plot(x, y)
plt.title("Jumlah Penjualan Kopi Instant Per Bulan", pad=10, fontsize=12, color="blue")
plt.xlabel("Bulan", fontsize=11)
plt.ylabel("Jumlah",fontsize=11)
plt.grid(color="gray", linestyle="-", linewidth=0.5)
plt.tight_layout()
plt.show()
