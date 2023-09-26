# =====  Praktikum  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
print(dqlabregex)

# =====  Tantangan Pertama Sunyi  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
#Buat kolom baru kota_awalan_J_S
dqlabregex['kota_awalan_j_s'] = dqlabregex['kota'].str.contains('^(j|s)', case = False)
print(dqlabregex[['kota','kota_awalan_j_s']])

# =====  Praktikum 1  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
#Buat kolom baru pencatat_senja
dqlabregex['pencatat_senja'] = dqlabregex['staf_pencatat'].str.contains('Sen.?ja')
print(dqlabregex[['staf_pencatat','pencatat_senja']])

# =====  Praktikum 2  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
#Buat kolom baru char_nonnumerik untuk mengetahui jumlah_member non numerik
dqlabregex['char_nonnumerik'] = dqlabregex['jumlah_member'].str.contains('[^0-9]')
print(dqlabregex[['jumlah_member','char_nonnumerik']])

# =====  Tantangan Kedua Sunyi  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
#Ubah kata Sendja, dsb menjadi Senja pada kolom staf_pencatat
dqlabregex['staf_pencatat'] = dqlabregex['staf_pencatat'].str.replace('Sen.?ja', 'Senja')
print(dqlabregex['staf_pencatat'])

# =====  Tantangan Ketiga Sunyi  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
#Ubah karakter pada kolom jumlah_member sesuai ketentuan
mapchange = {'O':'0','I':'1','S':'5'}
dqlabregex['jumlah_member_clean'] = dqlabregex['jumlah_member']
for ubah, pengubah in mapchange.items():
	dqlabregex['jumlah_member_clean'] = dqlabregex['jumlah_member_clean'].str.replace(ubah,pengubah, case = False)
print(dqlabregex[['jumlah_member','jumlah_member_clean']])

# =====  Praktikum 3  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
#Sintaks menghapus karakter non-numerik pada kolom jumlah_member
dqlabregex['jumlah_member'] = dqlabregex['jumlah_member'].str.replace('[^0-9]+','')
print(dqlabregex['jumlah_member'])

# =====  Praktikum 4  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
#Sintaks merapikan format tanggal pada kolom tanggal_catat
dqlabregex['tanggal_catat'] = dqlabregex['tanggal_catat'].str.replace('([0-9]{2})-([0-9]{2})-([0-9]{4})','\\2/\\1/\\3')
print(dqlabregex['tanggal_catat'])

# =====  Ready To Use Data  =====
import pandas as pd
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')
print("Tabel A:")
print(dqlabregex)
#Ubah karakter pada kolom jumlah_member sesuai ketentuan
mapchange = {'([0-9]{2})-([0-9]{2})-([0-9]{4})':'\\3-\\2-\\1','([0-9]{2})/([0-9]{2})/([0-9]{4})':'\\3-\\1-\\2'}
for ubah, pengubah in mapchange.items():
	dqlabregex['tanggal_catat'] = dqlabregex['tanggal_catat'].str.replace(ubah,pengubah)
#Ubah menjadi tipedata datetime pada kolom tanggal_catat
dqlabregex['tanggal_catat'] = pd.to_datetime(dqlabregex['tanggal_catat'])
#Hapus karakter non numerik pada kolom jumlah_member dan ubah tipedatanya menjadi integer
dqlabregex['jumlah_member'] = dqlabregex['jumlah_member'].str.replace('[^0-9]+','')
dqlabregex['jumlah_member'] = dqlabregex['jumlah_member'].astype(int)
#Ubah kata Sendja ataupun padanannya menjadi satu kata 'Senja' pada kolom staf_pencatat
dqlabregex['staf_pencatat'] = dqlabregex['staf_pencatat'].str.replace('Sen.?ja', 'Senja')
print("\nTabel B:")
print(dqlabregex) 
