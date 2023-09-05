# Praktik melalui Python untuk Klasifikasi Data Survei
# Berdasarkan pihak pengumpul data. Data mu ini jenisnya apa?
pihak = 'primer'
print("Berdasarkan pihak pengumpul data:", pihak)
# Berdasarkan sumber data. Data mu ini jenisnya apa?
sumber = 'eksternal'
print("\nBerdasarkan sumber data:", sumber)
# Nama-nama kolom: jenis_kelamin, umur_tahun, jenis_pekerjaan,
#   cek_medis, tinggi_badan_cm, berat_badan_kg
# Atribut/kolom dengan data kuantitatif?
data_kuantitatif = ['umur_tahun', 'tinggi_badan_cm', 'berat_badan_kg']
print("\nAtribut/kolom dengan data kuantitatif:\n ", data_kuantitatif)

# Skala Pengukuran Data: Praktik dengan Data Survei
# Skala nominal/kategorikal
nominal = ['jenis_kelamin', 'jenis_pekerjaan']
print("Kolom dengan skala nominal/kategorikal:\n ", nominal)
# Skala ordinal
ordinal = 'cek_medis'
print("\nKolom dengan skala ordinal:\n ", ordinal)
# Skala interval
interval = None
print("\nKolom dengan skala interval:\n ", interval)
# Skala rasio
rasio = ['umur_tahun', 'tinggi_badan_cm', 'berat_badan_kg']
print("\nKolom dengan skala rasio:\n ", rasio)

# Data Nominal di Pandas - Praktik
# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data jenis_kelamin
gender = ["Pria", "Pria", "Wanita", "Pria", "Wanita",
          "Wanita", "Wanita", "Pria", "Pria", "Wanita"]
df = pd.DataFrame({"jenis_kelamin": gender})
# Cek tipe data
print("Cek tipe data awal:\n ", df.dtypes)
# Buat kategori untuk kolom jenis_kelamin
cat = pd.CategoricalDtype(["Pria", "Wanita"])
# Ubahlah tipe data kolom jenis_kelamin
df = df.astype({"jenis_kelamin": cat})
# Cek kembali tipe data
print("\nCek tipe data setelah diubah:\n ", df.dtypes)

# Data Ordinal di Pandas - Praktik
# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data jenis_kelamin
gender = ["Pria", "Pria", "Wanita", "Pria", "Wanita",
          "Wanita", "Wanita", "Pria", "Pria", "Wanita"]
# Data cek medis
mcu = ["tidak pernah", "rutin (1 tahun sekali)",
       "tidak tentu waktunya", "tidak pernah", 
       "rutin (1 tahun sekali)", "lebih dari 2 tahun sekali",
       "tidak pernah", "tidak pernah", 
       "rutin (1 tahun sekali)", "2 tahun sekali"]
# Data frame
df = pd.DataFrame({"jenis_kelamin": gender,
                   "cek_medis": mcu})
# Cek tipe data
print("Cek tipe data awal:\n", df.dtypes)
# Buat kategori untuk kolom jenis_kelamin
cat = pd.CategoricalDtype(["Pria", "Wanita"])
# Buat kategori berurut untuk kolom cek_medis
ordl = pd.CategoricalDtype(["tidak pernah", 
                            "tidak tentu waktunya",
                            "lebih dari 2 tahun sekali",
                            "2 tahun sekali",
                            "rutin (1 tahun sekali)"], ordered=True)
# Ubahlah tipe data kolom jenis_kelamin dan cek_medis
df = df.astype({"jenis_kelamin": cat,
                "cek_medis": ordl})
# Cek kembali tipe data
print("\nCek tipe data setelah diubah:\n", df.dtypes)
print("\n", df["cek_medis"].head(3))

# pandas.cut untuk Data Berkelompok - Praktik
# Importlah pandas sebagai aliasnya pd
import pandas as pd
# Data berat badan 120 orang 
bb120 = [71.2, 66.8, 66.9, 65.9, 69.7, 63.4, 71.5, 66.5, 68.6, 67.5, 
         70.9, 63.9, 67.4, 67.2, 70.3, 65.8, 67.7, 66.2, 68.1, 69.2, 
         65.8, 70.3, 69.8, 69.0, 69.8, 66.6, 67.8, 66.1, 67.5, 69.1, 
         66.6, 67.2, 66.6, 66.3, 66.7, 68.0, 65.8, 68.5, 71.3, 69.5, 
         67.6, 66.2, 66.5, 71.4, 68.1, 66.7, 68.4, 72.2, 68.2, 69.2, 
         68.6, 67.3, 65.7, 67.3, 67.6, 69.2, 69.7, 69.9, 68.6, 69.8, 
         66.5, 70.5, 69.0, 67.4, 69.0, 67.8, 70.3, 71.0, 72.4, 65.2, 
         65.1, 67.0, 68.3, 69.8, 68.6, 64.0, 67.4, 69.7, 68.5, 69.5, 
         67.6, 67.6, 68.4, 68.8, 68.4, 68.2, 66.7, 68.8, 68.2, 70.3, 
         70.4, 68.4, 67.2, 66.7, 68.8, 68.2, 67.3, 68.1, 66.8, 69.4, 
         67.1, 70.4, 68.8, 69.2, 65.8, 68.3, 69.5, 66.1, 67.5, 68.1, 
         65.3, 68.6, 69.7, 66.3, 68.7, 65.4, 67.9, 64.8, 70.2, 68.8]
# Bin dengan menggunakan urutan bilangan (menggunakan list)
# yang sesuai dengan tabel yang dicontohkan
bin_list = list(range(63, 74))
print("bin berat badan dalam urutan bilangan:\n", bin_list)
# Buatlah kelompok data seperti tabel yang ditunjukkan
bin_bb = pd.cut(bb120, bin_list, right=False, include_lowest=True)
# Ubah bb120 ke dalam pandas.DataFrame
df_bb120 = pd.DataFrame(bb120)
# Kelompokkanlah df_bb120 ke dalam bin yang telah disediakan
tabel_bb = df_bb120.groupby(bin_bb).count()
# Untuk menset header dari tabel_bb
tabel_bb.rename(columns={0: "frekuensi"}, inplace=True)
tabel_bb.index.rename("rentang berat badan [kg]", inplace=True)
print("\nData berkelompok berat badan 120 orang:\n", tabel_bb)
