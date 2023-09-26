# =====  Import Package dan Menggunakan modul  =====
import math
print("Nilai pi adalah:", math.pi)# math.pi merupakan sintak untuk memanggil fungsi

# =====  Import dengan Module Rename atau Alias  =====
# menggunakan m sebagai module rename atau alias
import math as m
# m.pi merupakan sintak untuk memanggil fungsi
print("Nilai pi adalah:", m.pi)

# =====  Import Sebagian Fungsi  =====
from math import pi
print("Nilai pi adalah", pi)

# =====  Import Semua isi Moduls  =====
from math import *
print("Nilai e adalah:", e)
