# =====  Membuat fungsi sendiri  =====
# Membuat Fungsi
def salam():
    print("Hello, Selamat Pagi")
## Pemanggilan Fungsi
salam()

# =====  Parameter pada fungsi  =====
def luas_segitiga(alas, tinggi): # alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas);
# Pemanggilan fungsi
## 4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
luas_segitiga(4, 6) 

# =====  Fungsi dengan Return Value  =====
# alas dan tinggi merupakan parameter yang masuk
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    return luas
# Pemanggilan fungsi
## 4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga 
print("Luas segitiga: %d" % luas_segitiga(4, 6))
