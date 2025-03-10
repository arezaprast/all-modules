#--- Membaca ---
#meng-import library pandas, library ini dapat kita gunakan untuk membaca data dalam format excel
import pandas as pd
pd.set_option('display.max_column', 20)
#men-load file churn_analysis_train.xlsx sebagai pandas data frame untuk mempermudah proses pengolahan data
df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/cth_churn_analysis_train.xlsx')
#perintah untuk menampilkan 5 data pertama 
print(df.head())

#--- Mengubah Kolom Non-Numerik Menjadi Kolom Numerik ---
#Kode program sebelumnya
import pandas as pd
pd.set_option('display.max_column', 20)
df = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/cth_churn_analysis_train.xlsx')
#menghilangkan kolom id dari data frame dikarenakan kolom id tidak relevan untuk dijadikan input ataupun output dalam tugas klasifikasi
df.drop('ID_Customer', axis=1, inplace=True)
#mengubah nilai "Perempuan" menjadi 1 dan "Laki-laki" menjadi 0
df['Jenis_kelamin']= df['Jenis_kelamin'].map(
	lambda value: 1 if value == 'Perempuan' else 0)
#mengubah nilai using_reward "Yes" menjadi 1 dan "No" menjadi 0
df['using_reward']= df['using_reward'].map(
	lambda value: 1 if value == 'Yes' else 0)
#mengubah nilai pembayaran "Credit" menjadi 2, "Bank Transfer" menjadi 1 dan "Cash" menjadi 0
df['pembayaran']= df['pembayaran'].map(
    lambda value: 2 if value == 'Credit'
    else 1 if value == 'Bank Transfer'
    else 0)
#mengubah nilai subskripsi brosur "No" menjadi 0 dan nilai lainnya ("Email" dan "Yes") menjadi 1
df['Subscribe_brochure']= df['Subscribe_brochure'].map(
    lambda value: 0 if value == 'No'  else 1)
#mengubah nilai "Yes" menjadi 1 dan "No" menjadi 0
df['churn'] = df['churn'].map(
	lambda value: 1 if value == 'Yes' else 0)
#menampilkan isi dari variabel 'df' setelah perubahan
print(df.head())

#--- Feature Matrix dan Target ---
#Kode program sebelumnya
#menyimpan atribut diagnosis ke dalam variabel y dan disimpan ke dalam array 1D atau array target
y = df.pop('churn').to_numpy()
#mengubah seluruh data dalam df ke dalam format array 2D atau matrix feature X (jumlah data, jumlah atribut)
X = df.to_numpy()
#memastikan jumlah data dan jumlah atribut data input
print('X:', X.shape)
#memastikan jumlah data pada variabel y
print('y:', y.shape)

#--- Akurasi Data Training ---
#Kode program sebelumnya
#mengimport model 'DecisionTreeClassifier' dari library scikit-learn tepatnya dari modul tree.
from sklearn.tree import DecisionTreeClassifier
#inisialisasi model
model = DecisionTreeClassifier(random_state=12)
#melatih model berdasarkan data input (X) dan label (y)
model.fit(X, y)
#melakukan prediksi terhadap setiap data dalam X dan menyimpan hasil prediksi dalam array 'y_pred'
y_pred = model.predict(X)
#mengimport fungsi untuk menghitung akurasi dari library scikit-learn tepatnya dari modul metrics.
from sklearn.metrics import accuracy_score
#menghitung nilai akurasi dari hasil prediksi (y_pred) dengan label aktual yang dimiliki oleh setiap data (y) nilai akurasi dihitung dengan menggunakan total prediksi benar dibagi dengan total data yang diprediksi
score = accuracy_score(y,y_pred)
#menampilkan hasil akurasi dalam persen
print('Hasil akurasi model: %.2f %%' % (100*score))

#--- Train and Test Split - Praktikum ---
#Kode program sebelumnya
#fungsi untuk membagi data dan label ke dalam dua bagian (data latih dan data testing) secara acak tersedia dalam library scikit-learn.model_selection 
from sklearn.model_selection import train_test_split
#X_train dan y_train akan kita gunakan sebagai data untuk melatih model X_test dan y_test akan kita gunakan sebagai data testing untuk mengetahui kemampuan model untuk data yang belum pernah ia jumpai
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=12)
#melatih model berdasarkan data latih (X_train) dan labelnya (y_train)
model.fit(X_train, y_train)
#melakukan prediksi terhadap setiap data testing (X_test) dan menyimpan hasil prediksi dalam array 'y_pred'
y_pred = model.predict(X_test)
#mengimport fungsi untuk menghitung akurasi dari library scikit-learn tepatnya dari modul metrics.
from sklearn.metrics import accuracy_score
#menghitung nilai akurasi dari hasil prediksi (y_pred) dengan label aktual yang dimiliki oleh setiap data test (y_test)
score = accuracy_score(y_test,y_pred)
#menampilkan hasil akurasi dalam persen
print('Hasil akurasi model: %.2f %%' % (100*score))
