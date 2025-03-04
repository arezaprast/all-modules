#--- Implementasi Confusion Matrix ---
#Impor paket yang dibutuhkan
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#Baca dataset yang disimpan dalam sebuah file CSV hasil_uji.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/hasil_uji.csv')
y_actual = df['actual']
y_predict = df['predicted']
print(df.head())

#--- Membuat Confusion Matrix ---
#Kode sebelumnya
#Penamaan label pada tiap kelas
#Pilih nilai pada label
labels = list(y_actual.unique())
#Urutkan risiko dari nilai terendah ke nilai tertinggi
labels.sort()
#Dapatkan confusion matrix
confusion_matrix = metrics.confusion_matrix(y_actual, y_predict)
#Ubah menjadi sebuah dataframe
matrix_df = pd.DataFrame(confusion_matrix)
#Plot hasilnya
fig, ax = plt.subplots(figsize=(7,5))
sns.set(font_scale=1.3)
#Plot heatmap dengan anotasi jumlah data dengan format 'd' (decimal integer) di tiap sel
sns.heatmap(matrix_df, annot=True, fmt="d", ax=ax, cmap="magma")
#Tentukan judul gambar dan label pada sumbu x dan y
ax.set_title('Confusion Matrix - Decision Tree')
ax.set_xlabel("Predicted Risk Level", fontsize =15)
ax.set_xticklabels(list(labels))
ax.set_ylabel("Actual Risk Level", fontsize=15)
ax.set_yticklabels(list(labels), rotation = 0)
plt.show()

#--- Menghitung Nilai Accuracy Model ---
#Impor paket yang dibutuhkan
import pandas as pd
from sklearn import metrics
#Unggah dataset yang disimpan dalam sebuah file CSV hasil_uji.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/hasil_uji.csv')
y_actual = df['actual']
y_predict = df['predicted']
#Hitung nilai akurasi dari model
accuracy = metrics.accuracy_score(y_actual, y_predict)
print('Akurasi model: %.5f.' % accuracy)

#--- Menghitung Nilai Precision Setiap Kelas ---
#Impor paket yang dibutuhkan
import pandas as pd
from sklearn import metrics
#Unggah dataset yang disimpan dalam sebuah file CSV hasil_uji.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/hasil_uji.csv')
y_actual = df['actual']
y_predict = df['predicted']
#Penamaan label pada tiap kelas
#Pilih nilai pada label
labels = list(y_actual.unique())
#Urutkan risiko dari nilai terendah ke nilai tertinggi
labels.sort()
#Hitung nilai Precision pada tiap kelas, pilih average = None supaya menampilkan nilai presisi dari tiap kelas
precision = metrics.precision_score(y_actual, y_predict, average=None)
#Ubah menjadi sebuah dataframe
precision_results = pd.DataFrame(precision, index=labels)
#Ubah nama pada kolom hasil
precision_results.rename(columns={0:'precision'}, inplace=True)
print('Precision setiap kelas:\n', precision_results)

#--- Menghitung Nilai Recall Model ---
#Impor paket yang dibutuhkan
import pandas as pd
from sklearn import metrics
#Unggah dataset yang disimpan dalam sebuah file CSV hasil_uji.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/hasil_uji.csv')
y_actual = df['actual']
y_predict = df['predicted']
#Penamaan label pada tiap kelas
#Pilih nilai pada label
labels = list(y_actual.unique())
#Urutkan risiko dari nilai terendah ke nilai tertinggi
labels.sort()
#Hitung nilai Recall pada tiap kelas dan pilih average=None untuk menampilkan nilai recall dari tiap kelas
recall = metrics.recall_score(y_actual, y_predict, average=None)
#Ubah menjadi sebuah dataframe
recall_results = pd.DataFrame(recall, index=labels)
#Ubah nama pada kolom hasil
recall_results.rename(columns ={0:'Recall'}, inplace=True)
print('Recall:\n', recall_results)

#--- Menghitung Nilai F1-Score Model ---
#Impor paket yang dibutuhkan
import pandas as pd
from sklearn import metrics
#Unggah dataset yang disimpan dalam sebuah file CSV hasil_uji.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/hasil_uji.csv')
y_actual = df['actual']
y_predict = df['predicted']
#Penamaan label pada tiap kelas
#Pilih nilai pada label
labels = list(y_actual.unique())
#Urutkan risiko dari nilai terendah ke nilai tertinggi
labels.sort()
#Hitung nilai F1 pada tiap kelas dan pilih average=None untuk menampilkan nilai F1 dari tiap kelas
f1 = metrics.f1_score(y_actual, y_predict, average=None)
#Ubah menjadi sebuah dataframe
f1_results = pd.DataFrame(f1, index=labels)
#Ubah nama pada kolom hasil
f1_results.rename(columns={0:'f1'}, inplace=True)
print('F1-score:\n', f1_results)

#--- Recall, Precision, dan F1-score dalam 1 Laporan ---
#Impor paket yang dibutuhkan
import pandas as pd
from sklearn import metrics
#Unggah dataset yang disimpan dalam sebuah file CSV hasil_uji.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/hasil_uji.csv')
y_actual = df['actual']
y_predict = df['predicted']
#Hitung nilai recall, precision, dan f1-score
class_report = metrics.classification_report(y_actual, y_predict)
print('Classification report:\n', class_report)
