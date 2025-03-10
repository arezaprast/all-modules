#--- Implementasi Elbow Method ---
#Import library pandas
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
#Drop kolom customer_id
RFM_km = data.drop(["customer_id"], axis=1)
#Penerapan RobustScaler
from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
RFM_robust = robust_scaler.fit_transform(RFM_km)
RFM_robust = pd.DataFrame(RFM_robust)
RFM_robust.columns = ["Frequency","Recency","Monetary"]
#Import library Kmeans
from sklearn.cluster import KMeans
#Membuat variable SSE untuk menampung nilai WSS dari setiap nilai k 
SSE = []
#Melakukan k-means berulang dengan nilai k yang berbeda-beda dari 2 sampai 10
for k in range(2, 10):
    k_means = KMeans(n_clusters=k, random_state=0)
    model = k_means.fit(RFM_robust)
    SSE.append(k_means.inertia_)
#Mengkonversi hasil ke dalam data frame, kemudian menampilkannya dalam bentuk plot
import matplotlib.pyplot as plt
frame = pd.DataFrame({"Cluster":range(2,10), "SSE":SSE})
plt.figure(figsize=(8,5))
plt.plot(frame["Cluster"], frame["SSE"], marker="o")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

#--- Clustering K-Means dengan 3 Cluster ---
#Import library pandas
#Import library robust scaler
#Import library Kmeans
from sklearn.cluster import KMeans
#Menjalankan k-means dengan nilai k = 3
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(RFM_robust)
#pred menyimpan hasil prediksi label cluster untuk setiap data
pred = k_means.predict(RFM_robust)
#Menggabungkan RFM dan hasil label clustering
RFM_labeled = pd.concat([data, pd.Series(pred).rename("cluster")], axis=1)
#Menghitung jumlah data dari tiap cluster
print("Jumlah data dari tiap cluster:")
print(RFM_labeled['cluster'].value_counts())

#--- Visualisasi Box Plot untuk 3 Cluster ---
#Import library pandas
#Penerapan RobustScaler
#Import library Kmeans
# menjalankan k-means dengan nilai k = 3
#pred menyimpan hasil prediksi label cluster untuk setiap data
#Menggabungkan RFM dan hasil label clustering
#Import library matplotlib dan seaborn
import matplotlib.pyplot as plt
import seaborn as sns
#Menampilkan boxplot elbow method
fig, ax = plt.subplots(1, 3, figsize=(8,6))
sns.boxplot(x="cluster", y="frequency", data=RFM_labeled, ax=ax[0])
sns.boxplot(x="cluster", y="recency", data=RFM_labeled, ax=ax[1])
sns.boxplot(x="cluster", y="monetary", data=RFM_labeled, ax=ax[2])
plt.tight_layout()
plt.show()

#--- Implementasi Silhouette Method ---
#Import library pandas
#Drop kolom customer_id
#Penerapan RobustScaler
#Import KMeans & silhouette_score
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
#Melakukan k-means berkali-kali dengan nilai k yang berbeda-beda dari 2 sampai 15
silhouette = []
for k in range(2, 15):
    k_means = KMeans(n_clusters=k, random_state=0)
    model = k_means.fit(RFM_robust)
    silhouette.append(silhouette_score(RFM_robust, model.labels_))
#Import library matplotlib
import matplotlib.pyplot as plt
#Mengkonversi hasil ke dalam data frame, kemudian menampilkannya dalam bentuk plot
frame = pd.DataFrame({"Cluster":range(2,15), "Silhouette Score":silhouette})
plt.figure(figsize=(8,5))
plt.plot(frame["Cluster"], frame["Silhouette Score"], marker="o")
plt.xlabel("Number of clusters")
plt.ylabel("Silhouette Score")
plt.show()

#--- Clustering K-Means dengan 4 Cluster ---
#Import library pandas
#Drop kolom customer_id
#Penerapan RobustScaler
#Import KMeans & silhouette_score
#Menjalankan k-means dengan nilai k = 4
k_means = KMeans(n_clusters=4, random_state=0)
k_means.fit(RFM_robust)
#Pred menyimpan hasil prediksi label cluster untuk setiap data
pred = k_means.predict(RFM_robust)
#Menggabungkan dataframe data dan hasil label clustering
RFM_labeled = pd.concat([data, pd.Series(pred).rename("cluster")], axis=1)
#Menghitung jumlah data dari tiap cluster
print("Jumlah data dari tiap cluster:")
print(RFM_labeled['cluster'].value_counts())

#--- Visualisasi Box Plot untuk 4 Cluster ---
#Import library pandas
#Drop kolom customer_id
#Penerapan RobustScaler
#Import KMeans & silhouette_score
#Menjalankan k-means dengan nilai k = 4
#Pred menyimpan hasil prediksi label cluster untuk setiap data
#Menggabungkan dataframe data dan hasil label clustering
#Import library matplotlib dan seaborn
import matplotlib.pyplot as plt
import seaborn as sns
#Menampilkan boxplot silhouette method
fig, ax = plt.subplots(1, 3, figsize=(8,6))
sns.boxplot(x="cluster", y="frequency", data=RFM_labeled, ax=ax[0])
sns.boxplot(x="cluster", y="recency", data=RFM_labeled, ax=ax[1])
sns.boxplot(x="cluster", y="monetary", data=RFM_labeled, ax=ax[2])
plt.tight_layout()
plt.show()
