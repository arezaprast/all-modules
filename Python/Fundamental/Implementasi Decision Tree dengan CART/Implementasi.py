#--- Membaca dan Menampilkan Data ---
#Impor library pandas yang akan digunakan untuk mengolah data menggunakan struktur dataframe
import pandas as pd
pd.set_option('display.max_column', 20)
#Unggah dataset yang disimpan dalam sebuah file Excel
df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/credit_scoring_dqlab.xlsx')
#Periksa sampel dari dataset dengan menjalankan perintah df.head()
print(df.head())

#--- Drop Kolom dan Melihat Relasi Antar Data ---
#Kode sebelumnya
#Hapus kolom kode_kontrak dari dataframe
df.drop(['kode_kontrak'], axis=1, inplace=True)
#Periksa relasi antara kolom 'rata_rata_overdue' dan 'risk_rating'
print('melihat data unique pada kolom rata_rata_overdue:')
print(df['rata_rata_overdue'].unique())
print()
print('melihat data unique pada kolom risk_rating:')
print(df['risk_rating'].unique())
print()
print('membandingkan data pada kolom rata_rata_overdue dan risk_rating:')
print(df[['rata_rata_overdue','risk_rating']])

#--- Menghapus Kolom 'rata_rata_overdue' ---
#Kode sebelumnya
#Hapus kolom rata_rata_overdue dari dataframe
df.drop(['rata_rata_overdue'], axis=1, inplace=True)
#Memeriksa jumlah data pada setiap kelas
print(df['risk_rating'].value_counts())

#--- Memeriksa Data ---
#Kode sebelumnya
#Periksa struktur dataset
df.info()
#Periksa data unique pada kolom kpr_aktif
print('\nData unik pada kpr_aktif:', df['kpr_aktif'].unique())
#Periksa tipe data pada kolom kpr_aktif
print('\nTipe Data:', type(df['kpr_aktif'].iloc[1]))

#--- Konversi Tipe Data String ke Boolean ---
#Kode sebelumnya
#Konversi tipe data 'kpr_aktif' dari tipe string menjadi boolean
df.loc[(df['kpr_aktif']=='YA'), 'kpr_aktif'] = True
df.loc[(df['kpr_aktif']=='TIDAK'), 'kpr_aktif'] = False
df['kpr_aktif'] = df['kpr_aktif'].astype('bool')
df.info()

#--- Pembagian Dataset Training dan Testing ---
#Kode sebelumnya
#Membagi kolom menjadi variabel fitur dan variabel target
feature_cols = ['pendapatan_setahun_juta', 'kpr_aktif', 'durasi_pinjaman_bulan', 'jumlah_tanggungan']
# Variabel fitur
X = df[feature_cols]
# Variabel target
y = df['risk_rating']
#Bagi dataset menjadi training (60%) dan testing set (40%) dan seed untuk random number=42 (seed boleh bebas dipilih)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
#Cek ukuran training set dan testing set
print('Ukuran training set:', X_train.shape)
print('Ukuran testing set :', X_test.shape)

#--- Cek Porsi Data Training dan Testing ---
#Kode sebelumnya
#Cek porsi tiap kelas pada data training dan data testing
print('Porsi tiap kelas pada data training:')
print(y_train.value_counts(normalize=True) * 100)
print('\nPorsi tiap kelas pada data testing:')
print(y_test.value_counts(normalize=True) * 100)

#--- Inisialisasi dan Pelatihan Model ---
#Kode sebelumnya
#Melakukan import library DecisionTreeClassifier dari paket sklearn.tree
from sklearn.tree import DecisionTreeClassifier
#Buat sebuah Decision Tree Classifier dengan metode gini impurity index, kedalaman pohon = 4 dan seed bilangan acak = 42
#Lakukan fitting model DTS dengan menggunakan training data
clf = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)
#Melakukan fitting model dengan dataset training
clf.fit(X_train, y_train)
print(clf)

#--- Visualisasi Model #1 ---
#Kode sebelumnya
#Melakukan labeling pada Decision Tree
feature_names = X.columns
labels = list(y.unique())
labels.sort()
labels = [str(x) for x in labels]
#Visualisasi Decision Tree Classifier menggunakan library 'tree' impor paket yang dibutuhkan
from sklearn import tree
import matplotlib.pyplot as plt
#plot gambar dan atur warna latar
plt.figure(figsize=(30,10), facecolor ='yellow')
#Buat diagram pohon
tree.plot_tree(clf, feature_names=feature_names, class_names=labels, rounded=True, filled=True, fontsize=8)
#Apabila gambar pohon yang dihasilkan tidak jelas, gambar tersebut dapat disimpan dengan resolusi tinggi ke dalam bentuk JPEG, PNG, dsb. Gambar dapat dilihat pada file yang telah disimpan
#plt.savefig("nama_file.png", dpi=100)
#Tampilkan gambar
plt.tight_layout()
plt.show()

#--- Visualisasi Model #2 ---
#Kode sebelumnya
#Visualisasi Decision Tree menggunakan text
#import relevant functions
from sklearn.tree import export_text
#export the decision rules
tree_rules = export_text(clf, feature_names=list(X.columns))
#print the result
print(tree_rules)

#--- Evaluasi Model ---
#Kode sebelumnya
#Lakukan prediksi dataset training menggunakan model yang telah dibangun
from sklearn import metrics 
train_pred = clf.predict(X_train)
train_accuracy = metrics.accuracy_score(y_train, train_pred)
print('Akurasi training dataset:', train_accuracy)
#Lakukan prediksi dataset testing menggunakan model yang telah dibangun
test_pred = clf.predict(X_test)
test_accuracy = metrics.accuracy_score(y_test, test_pred)
print('Akurasi testing dataset :', test_accuracy)

#--- Hyperparameter Tuning ---
#Kode sebelumnya
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics 
df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/credit_scoring_dqlab.xlsx')
df.drop(['kode_kontrak'], axis=1, inplace=True)
df.drop(['rata_rata_overdue'], axis=1, inplace=True)
df.loc[(df['kpr_aktif']=='YA'), 'kpr_aktif'] = True
df.loc[(df['kpr_aktif']=='TIDAK'), 'kpr_aktif'] = False
df['kpr_aktif'] = df['kpr_aktif'].astype('bool')
feature_cols = ['pendapatan_setahun_juta', 'kpr_aktif', 'durasi_pinjaman_bulan', 'jumlah_tanggungan']
X = df[feature_cols]
y = df['risk_rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
#Impor fungsi GridSearchCV
from sklearn.model_selection import GridSearchCV
#Tentukan nilai parameter max_depth yang akan diuji
tuned_parameters = [{'max_depth': [1,2,3,4,5,6,7,8,9,10]}]
#Tentukan kriteria penilaian menggunakan nilai F1
print('\nTuning hyperparameters untuk F1-score\n')
clf = GridSearchCV(DecisionTreeClassifier(), tuned_parameters, scoring='f1_macro')
clf.fit(X_train, y_train)
print('Hasil nilai uji saat melakukan tuning:')
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
	print(f'{mean:0.3f} (+/-{std*2:0.03f}) for {params}')
#Parameter terbaik yang ditemukan
print('\nParameter terbaik yang ditemukan:')
print(clf.best_params_)
#Model dengan parameter terbaik yang ditemukan
best_model = clf.best_estimator_
#Lakukan prediksi dataset training dan dataset testing menggunakan model dengan parameter terbaik
train_pred = best_model.predict(X_train)
train_accuracy = metrics.accuracy_score(y_train, train_pred)
test_pred = best_model.predict(X_test)
test_accuracy = metrics.accuracy_score(y_test, test_pred)
print('\nAkurasi training dataset:', train_accuracy)
print('Akurasi testing dataset :', test_accuracy)
