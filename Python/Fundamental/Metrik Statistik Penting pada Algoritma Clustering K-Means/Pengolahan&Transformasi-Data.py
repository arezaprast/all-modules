#--- Membaca Dataset ---
#Import library pandas
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
print(data.head(10))

#--- Melihat Dimensi Dataframe ---
#Melihat dimensi dataframe
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
print(data.shape)

#--- Melihat Tipe Data Dari Setiap Kolom ---
#Melihat tipe data dari setiap kolom
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
data.info()

#--- Melihat Statistik Dari Setiap Kolom ---
#Melihat statistik dari setiap kolom
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
print(data.describe())

#--- Melakukan Pengecekan Data Null ---
#Mengecek apakah ada data null
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
print(data.isnull().any().any())

#--- Membuang Kolom customer_id ---
#Menghapus kolom customer_id
import pandas as pd
data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/RFM_customer.csv", encoding='utf8')
RFM_km = data.drop(['customer_id'], axis=1)
print(RFM_km.head())

#--- Melihat Outliers pada Setiap Kolom ---
#Import library pandas
#Import library matplotlib.pyplot
import matplotlib.pyplot as plt
#Import library seaborn
import seaborn as sns
#Menampilkan boxplot data frequency, recency, dan monetary
fig, ax = plt.subplots(3, 1, figsize=(8,5))
sns.boxplot(RFM_km['frequency'], ax=ax[0])
sns.boxplot(RFM_km['recency'], ax=ax[1])
sns.boxplot(RFM_km['monetary'], ax=ax[2])
plt.tight_layout()
plt.show()

#--- Menggunakan RobustScaler() ---
#Import library pandas
#Import library robust scaler
from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
RFM_robust = robust_scaler.fit_transform(RFM_km)
RFM_robust = pd.DataFrame(RFM_robust)
RFM_robust.columns = ["Frequency","Recency","Monetary"]
#Import library matplotlib.pyplot dan seaborn
import matplotlib.pyplot as plt
import seaborn as sns
#Menampilkan boxplot data frequency, recency, dan monetary
fig, ax = plt.subplots(3, 1, figsize=(8,5))
sns.boxplot(RFM_robust["Frequency"], ax=ax[0])
sns.boxplot(RFM_robust["Recency"], ax=ax[1])
sns.boxplot(RFM_robust["Monetary"], ax=ax[2])
plt.tight_layout()
plt.show()
