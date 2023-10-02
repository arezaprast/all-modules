# =====  Simple Random Sampling Menggunakan Python  =====
import random
#Set seed sebagai bilangan bulat 0, dan dapat diganti
#dengan bilangan bulat lainnya, sesuai dengan instruksi Senja
random.seed(1234)
#Ambil sampel dalam rentang butir data, yaitu 1 s/d 120
#Inisialisasi sampel
sampel = []
#Looping sebanyak sampel yang ingin ditarik yaitu 10% (12 butir data)
for i in range(12): 
    sampel.append(random.randint(1, 120))
#Cetaklah sampel
print("sampel:", sampel)

# =====  Simple Random Sampling Menggunakan Numpy  =====
import numpy as np
#Set seed sebagai bilangan bulat 0, dan dapat diganti
#dengan bilangan bulat lainnya
np.random.seed(0)
#Ambil sampel dalam rentang butir data, yaitu 1 s/d 120,
#sebanyak 10% (12 butir data)
sampel = np.random.randint(1, 121, size=12)
#Cetaklah sampel
print("sampel:", sampel)

# =====  Menentukan Jumlah Sampel  =====
import math
# Jumlah anggota populasi
N = 8963
# Proporsi
p = 0.25
# z-score
z = 1.96
# Margin of error
e = 0.05
# Perhitungan ukuran sampel, n
n_aksen = z**2 * p * (1 - p) / e**2
n = n_aksen / (1 + (n_aksen / N))
# Cetak jumlah sampel
print("Jumlah sampel:", math.ceil(n))
