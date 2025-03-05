#--- Contoh Penggunaan Algoritma K-Means pada Python #1 ---
#Import make blobs agar dapat membuat sample data untuk clustering
from sklearn.datasets import make_blobs
#Features menyimpan numpy array 2 dimensi, true tabel berisikan label cluster dari setiap data
#Make_blobs digunakan untuk membuat sample data secara acak
features, true_labels = make_blobs(n_samples=200, centers=3, cluster_std=2, random_state=24)
#Untuk melihat sampel data ini (features dan label sebenarnya) dapat divisualisasikan ke dalam scatter plot 
#Import library seaborn dan matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
#Plotkan features yang telah dibuat dengan make_blobs dan bedakan warna dari 3 kelompok cluster data asal
sns.scatterplot(x=features[:,0], y=features[:,1], hue=true_labels)
plt.legend(loc="lower left")
plt.show()

#--- Contoh Penggunaan Algoritma K-Means pada Python #2 ---
#Import make_blobs agar dapat membuat sample data untuk clustering
from sklearn.datasets import make_blobs
#Features menyimpan numpy array 2 dimensi, true label berisikan label cluster dari setiap data
# make_blobs digunakan untuk membuat sample data secara acak
features, true_labels = make_blobs(n_samples=200, centers=3, cluster_std=2, random_state=24)
#Import StandardScaler untuk feature scaling
from sklearn.preprocessing import StandardScaler
#Transformasi fitur
StandardScaler = StandardScaler()
scaled_features = StandardScaler.fit_transform(features)
#Import KMeans untuk mengimplementasikan K-Means Clustering
from sklearn.cluster import KMeans
#Mengimplementasikan KMeans dengan membagi data ke dalam 3 cluster
kmeans = KMeans(n_clusters=3, random_state=24)
#Melakukan perhitungan cluster center, kemudian melakukan prediksi cluster untuk setiap data
result = kmeans.fit_predict(scaled_features)
#Import library seaborn dan matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
#Menampilkan data dan label clusternya, warna green cluster 0, warna blue cluster 1, warna red cluster 2
sns.scatterplot(x=scaled_features[:,0], y=scaled_features[:,1], hue=result)
#Menampilkan posisi cluster center
sns.scatterplot(x=kmeans.cluster_centers_[:,0], y=kmeans.cluster_centers_[:,1], s=200, marker="*", color="blue")
plt.legend(loc="lower left")
plt.show()

#--- Persiapan Dataset ---
#Import library pandas
import pandas as pd
#Membaca data
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Menampilkan 10 baris teratas
print(data.head(10))

#--- Melihat Tipe Data Dari Setiap Kolom ---
#Import library pandas
import pandas as pd
#Membaca data
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Melihat dimensi dataframe
print(data.shape)
# melihat tipe data dari setiap kolom
data.info()

#--- Melihat Statistik Dari Setiap Kolom ---
#Import library pandas
import pandas as pd
#Membaca data
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Untuk melihat statistik dari setiap kolom
print(data.describe())

#--- Missing Value dan Menghapus Kolom customer_id ---
#Import library pandas
import pandas as pd
#Membaca data
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Mengecek apakah ada data null
print(data.isnull().any().any())
#Menghapus kolom customer_id
RFM_km = data.drop(["customer_id"], axis=1)
print(RFM_km.head())

#--- Melakukan Standarisasi Data ---
#Import library pandas
import pandas as pd
#Membaca data
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Menghapus kolom customer_id
RFM_km = data.drop(["customer_id"], axis=1)
#Import StandardScaler
from sklearn.preprocessing import StandardScaler
standard_scaler = StandardScaler()
RFM_standardized = standard_scaler.fit_transform(RFM_km)
RFM_standardized = pd.DataFrame(RFM_standardized)
RFM_standardized.columns = ["Frequency","Monetary","Recency"]
print(RFM_standardized.head())

#--- Implementasi K-Means Clustering ---
#Import library pandas
import pandas as pd
#Membaca data
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Menghapus kolom customer_id
RFM_km = data.drop(["customer_id"], axis=1)
#Import StandardScaler
from sklearn.preprocessing import StandardScaler
standard_scaler = StandardScaler()
RFM_standardized = standard_scaler.fit_transform(RFM_km)
RFM_standardized = pd.DataFrame(RFM_standardized)
RFM_standardized.columns = ["Frequency","Monetary","Recency"]
#Import KMeans untuk mengimplementasikan K-Means Clustering
from sklearn.cluster import KMeans
#Mengatur parameter k-means, jumlah cluster yang akan dibentuk adalah 3
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(RFM_standardized)
#Pred menyimpan hasil prediksi label cluster untuk setiap data
pred = k_means.predict(RFM_standardized)
#Menggabungkan RFM dan hasil label clustering
RFM_labeled = pd.concat([RFM_standardized, pd.Series(pred).rename("cluster")], axis=1)
print(RFM_labeled.head())
#Menghitung jumlah data di setiap cluster
print(RFM_labeled["cluster"].value_counts())

#--- Menampilkan Box Plot ---
#Membaca data
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Menghapus kolom customer_id
RFM_km = data.drop(["customer_id"], axis=1)
#Import StandardScaler
from sklearn.preprocessing import StandardScaler
standard_scaler = StandardScaler()
RFM_standardized = standard_scaler.fit_transform(RFM_km)
RFM_standardized = pd.DataFrame(RFM_standardized)
RFM_standardized.columns = ["Frequency","Monetary","Recency"]
#Import KMeans untuk mengimplementasikan K-Means Clustering
from sklearn.cluster import KMeans
#Mengatur parameter k-means, jumlah cluster yang akan dibentuk adalah 3
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(RFM_standardized)
#Pred menyimpan hasil prediksi label cluster untuk setiap data
pred = k_means.predict(RFM_standardized)
#Menggabungkan RFM dan hasil label clustering
RFM_labeled = pd.concat([RFM_standardized, pd.Series(pred).rename("cluster")], axis=1)
#Import library matplotlib & seaborn
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots(1,3, figsize=(18,12))
#Menampilkan hasil clustering untuk setiap data dalam bentuk boxplot
sns.boxplot(x="cluster", y="Recency", data=RFM_labeled, ax=ax[0])
sns.boxplot(x="cluster", y="Frequency", data=RFM_labeled, ax=ax[1])
sns.boxplot(x="cluster", y="Monetary", data=RFM_labeled, ax=ax[2])
plt.show()
