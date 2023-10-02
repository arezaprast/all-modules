# =====  Membaca Dataset  =====
import pandas as pd
#load dataset ke dataframe anscombe
anscombe = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/anscombe.csv")
#menampilkan seluruh baris data yang ada
print("Anscombe's Quartet")
print(anscombe)
#menampilkan mean dataset anscombe
print("\nMean dari Anscombe's Quartet")
print(anscombe.mean())

# =====  Visualisasi Scatter  =====
import pandas as pd
#load dataset ke dataframe anscombe
anscombe = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/anscombe.csv")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
#scatter plot (x1, y1), (x2, y2), (x3, y3), dan (x4, y4)
ax[0][0].scatter(anscombe.x1, anscombe.y1)
ax[0][1].scatter(anscombe.x2, anscombe.y2)
ax[1][0].scatter(anscombe.x3, anscombe.y3)
ax[1][1].scatter(anscombe.x4, anscombe.y4)
k = 1
for i in range(2):
	for j in range(2):
		ax[i][j].set_xlabel("x" + str(k), fontsize=12)
		ax[i][j].set_ylabel("y" + str(k), fontsize=12)
		ax[i][j].grid()
		k += 1
plt.tight_layout()
plt.show()

# =====  Latihan  =====
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
#melakukan rename terhadap kolom "tinggi badan (cm)" menjadi "tinggi"
df.rename({'tinggi badan (cm)' : 'tinggi'}, axis=1, inplace=True)
#mendapatkan nilai mean menggunakan fungsi yang disediakan pandas
print(df["tinggi"].mean())
#mendapatkan nilai median menggunakan fungsi yang disediakan pandas
print(df["tinggi"].median())
#mendapatkan nilai modus menggunakan fungsi yang disediakan pandas
print(df["tinggi"].mode())
