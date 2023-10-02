# =====  Problem - 1  =====
import pandas as pd
tinggi_badan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
#Cetak type(tinggi_badan) dan data frame tinggi_badan sendiri
print("type(tinggi_badan):", type(tinggi_badan))
print(tinggi_badan)
#Hitung statistik deskriptif tinggi_badan
statistik_deskriptif = tinggi_badan.describe()
#Cetak statistik deskriptif tinggi_badan
print("\nStatistik deskriptif:\n", statistik_deskriptif)
#Tentukan IQR
Q1 = statistik_deskriptif["tinggi badan (cm)"]["25%"]
Q3 = statistik_deskriptif["tinggi badan (cm)"]["75%"]
IQR = Q3 - Q1
#Cetak IQR
print("\nIQR:", IQR)
#Persentil ke-5 dan ke-95
percentile = tinggi_badan.quantile(q=[0.05, 0.95])
print("\nPersentil ke-5 dan ke-95:\n", percentile)

# =====  Problem - 2  =====
import pandas as pd
tinggi_badan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
print("Statistik deskriptif data awal:\n", tinggi_badan.describe().T)
#Modifikasi data maksimum tinggi badan menjadi 186 cm
tinggi_badan_mod = tinggi_badan.replace(tinggi_badan.max(), 186)
print("\nStatistik deskriptif data modifikasi:\n", tinggi_badan_mod.describe().T)
import matplotlib.pyplot as plt
import seaborn as sns
fig, axs = plt.subplots(2, 1, figsize=(12,8), sharex=True)
#Plot data awal
sns.boxplot(data=tinggi_badan, x="tinggi badan (cm)", whis=1.5, color="yellowgreen", ax=axs[0])
sns.swarmplot(data=tinggi_badan, x="tinggi badan (cm)", size=8, color="darkcyan", edgecolor=None, ax=axs[0])
axs[0].grid(axis="x")
axs[0].set_xlabel(None)
axs[0].set_title("Data awal", color="darkcyan", fontsize=16)
#Plot data modifikasi
sns.boxplot(data=tinggi_badan_mod, x="tinggi badan (cm)", whis=1.5, color="yellowgreen", ax=axs[1])
sns.swarmplot(data=tinggi_badan_mod, x="tinggi badan (cm)", size=8, color="darkcyan", edgecolor=None, ax=axs[1])
axs[1].grid(axis="x")
axs[1].set_xlabel(None)
axs[1].set_title("Data modifikasi", color="darkcyan", fontsize=16)
plt.xlabel("Tinggi badan (cm)", fontsize=14)
plt.tight_layout()
plt.show()
