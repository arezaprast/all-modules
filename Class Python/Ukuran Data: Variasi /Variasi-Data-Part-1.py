# Membaca Dataset
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Cetak ukuran dataset dan isinya
print("Ukuran data tinggi_badan:", tinggi_badan.shape)
print("Data tinggi_badan (cm):\n", tinggi_badan)

# Rentang Data (Range)
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Tentukan rentang data
print("Range data:")
print("  min:", tinggi_badan.min())
print("  max:", tinggi_badan.max())

# Visualisasi Data dengan Swarmplot
import numpy as np
# Baca dataset
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Import matplotlib.pyplot dan seaborn sebagai aliasnya
import matplotlib.pyplot as plt
import seaborn as sns
# Visualisasikan dengan swarmplot variabel tinggi_badan dengan ukuran marker 8
fig, ax = plt.subplots(figsize=(10,4)) 
sns.swarmplot(x=tinggi_badan, size=8, color="darkcyan", edgecolor=None, ax=ax)
ax.grid(axis="x")
plt.xlabel("Tinggi badan (cm)", fontsize=14)
plt.tight_layout()
plt.show()

# Kuartil Data dengan numpy.percentile
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Perhitungan Q1, Q2, dan Q3 satu persatu
print("Perhitungan Q1, Q2, dan Q3 satu persatu")
Q1 = np.percentile(tinggi_badan, 25)
Q2 = np.percentile(tinggi_badan, 50)
Q3 = np.percentile(tinggi_badan, 75)
print("Kuartil 1 (Q1):", Q1)
print("Kuartil 2 (Q2):", Q2)
print("Kuartil 3 (Q3):", Q3)
# Perhitungan Q1, Q2, dan Q3 sekaligus
print("\nPerhitungan Q1, Q2, dan Q3 sekaligus")
Q123 = np.percentile(tinggi_badan, [25, 50, 75])
print("[Q1, Q2, Q3]:", Q123)

# Kuartil Data dengan numpy.quantile
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Perhitungan Q1, Q2, dan Q3 satu persatu
print("Perhitungan Q1, Q2, dan Q3 satu persatu")
Q1 = np.quantile(tinggi_badan, 0.25)
Q2 = np.quantile(tinggi_badan, 0.5)
Q3 = np.quantile(tinggi_badan, 0.75)
print("Kuartil 1 (Q1):", Q1)
print("Kuartil 2 (Q2):", Q2)
print("Kuartil 3 (Q3):", Q3)
# Perhitungan Q1, Q2, dan Q3 sekaligus
print("\nPerhitungan Q1, Q2, dan Q3 sekaligus")
Q123 = np.quantile(tinggi_badan, [0.25, 0.5, 0.75])
print("[Q1, Q2, Q3]:", Q123)

# Nilai Upper dan Lower Whisker
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Perhitungan Q1, Q2, dan Q3
Q1, Q2, Q3 = np.percentile(tinggi_badan, [25, 50, 75])
# Jarak antar kuartil (inter quartile range, IQR)
IQR = Q3 - Q1
print("Jarak antar kuartil (IQR):", IQR)
print("\nlower whisker:", Q1 - 1.5*IQR)
print("           Q1:", Q1)
print("           Q2:", Q2)
print("           Q3:", Q3)
print("upper whisker:", Q3 + 1.5*IQR)

# Visualisasi Data dengan Box Plot
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Import matplotlib.pyplot dan seaborn sebagai aliasnya 
import matplotlib.pyplot as plt
import seaborn as sns
ig, ax = plt.subplots(figsize=(10,4))
# Buatlah boxplot pada data tinggi_badan dengan nilai whis 1.5
sns.boxplot(x=tinggi_badan, whis=1.5, color="greenyellow", ax=ax)
# Plotkan kembali swarmplot
sns.swarmplot(x=tinggi_badan, size=8, color="darkcyan", edgecolor=None, ax=ax)
ax.grid(axis="x")
plt.xlabel("Tinggi badan (cm)", fontsize=14)
plt.tight_layout()
plt.show()

# Menentukan Persentil
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Persentil ke-5 dan ke-95
print("Menggunakan np.percentile")
P5, P95 = np.percentile(tinggi_badan, [5, 95])
print("  Persentil ke-5  (P5) :", P5)
print("  Persentil ke-95 (P95):", P95)
print("\nMenggunakan np.quantile")
P5, P95 = np.quantile(tinggi_badan, [0.05, 0.95])
print("  Persentil ke-5  (P5) :", P5)
print("  Persentil ke-95 (P95):", P95)
