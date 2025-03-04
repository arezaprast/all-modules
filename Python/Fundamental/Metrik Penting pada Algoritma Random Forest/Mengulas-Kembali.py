#--- Membaca Dataset ---
#mengimport library Pandas
import pandas as pd
pd.set_option('display.max_column', 10)
#membaca dataset credit_scoring_dqlab dari file excel
dataset_credit_scoring = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/credit_scoring_dqlab.xlsx')
print('Dataset credit scoring:')
print(dataset_credit_scoring)
print('\nInformasi dataset:')
dataset_credit_scoring.info()

#--- Mengubah Kolom kpr_aktif Menjadi Numerik ---
#Kode sebelumnya
#mengubah data kpr_aktif menjadi tipe integer
dataset_credit_scoring['kpr_aktif'].replace(['YA', 'TIDAK'],[1, 0], inplace=True)
print('Dataset credit scoring:')
print(dataset_credit_scoring)

#--- Mengubah Kolom rata_rata_overdue Menjadi Numerik ---
#Kode sebelumnya
# Label Encoding rata_rata_overdue, untuk menghilangkan value string, sehingga bisa dibuat dalam bentuk numeric array, dan tidak error saat membuat modelnya
dataset_credit_scoring['rata_rata_overdue'].replace({'0 - 30 days':1, '31 - 45 days':2, '46 - 60 days':3, '61 - 90 days':4, '> 90 days':5}, inplace=True)
print('Dataset credit scoring:')
print(dataset_credit_scoring)

#--- Feature Matrix X (Independent Variables) ---
#Kode sebelumnya
#untuk X (independent variables), data yang dimasukkan semua persyaratan untuk membuat risk_rating (variabel dependen), tidak memerlukan kode_kontrak, sehingga kolom kode_kontrak,  risk_rating, dan rata_rata_overdue dibuang
X=dataset_credit_scoring.drop(columns=['kode_kontrak', 'risk_rating', 'rata_rata_overdue']).values
print("Ukuran matrix feature X:", X.shape)

#--- Target y (Dependent Variable) ---
#Kode sebelumnya
#kolom Y (target/dependent variable) adalah target nilai yang harus dibuat sistem ketika membaca data X isinya adalah kolom risk_rating
y = dataset_credit_scoring['risk_rating'].values
print('Ukuran target y:', y.shape)

#--- Data Training dan Data Testing ---
#Kode sebelumnya
#membagi data training dan data testing, dimana training 70% dan testing 30%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#menampilkan jumlah data train dan test
print('Ukuran X_train:', X_train.shape)
print('Ukuran X_test :', X_test.shape)
print('Ukuran y_train:', y_train.shape)
print('Ukuran y_test :', y_test.shape)

#--- Membangun Random Forest Classifier ---
#Kode sebelumnya
#membangun Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
# Nilai Entropy menentukan bagaimana sebuah Decision Tree melakukan pemisahan data. Nilai Entropi berpengaruh ketika decision tree menentukan batasan/boundaries - nya. random_state digunakan untuk menentukan jumlah bootstrapping sample yang akan dilakukan. Nilai random state yang banyak digunakan adalah 0 dan 42.
rfc = RandomForestClassifier(criterion='entropy', random_state=42)
model = rfc.fit(X_train, y_train)
print(model)
