# =====  Matriks Korelasi  =====
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
plt.clf()
#mengatur ukuran gambar/plot
plt.rcParams['figure.dpi'] = 100
plt.figure()
plt.matshow(raw_data.corr())
plt.title('Plot correlation matriks dengan .matshow', size=14)
plt.tight_layout()
plt.show()
plt.figure()
sns.heatmap(raw_data.corr(), annot=True)
plt.title('Plot correlation matriks dengan sns.heatmap', size=14)
plt.tight_layout()
plt.show()

# =====  Grouped Box Plot  =====
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
plt.clf()
plt.figure()
#boxplot biasa tanpa pengelompokkan
raw_data.boxplot(rot=90)
plt.title('Boxplot tanpa pengelompokkan', size=14)
plt.tight_layout()
plt.show()
plt.figure()
#box plot dengan pengelompokkan dilakukan oleh kolom 'Produk'
raw_data.boxplot(by='Produk')
plt.tight_layout()
plt.show()

# =====  Grouped Histogram  =====
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
plt.clf()
plt.figure()
raw_data[raw_data['Produk'] == 'A'].hist()
plt.tight_layout()
plt.show()
plt.figure()
raw_data[raw_data['Produk'] == 'B'].hist()
plt.tight_layout()
plt.show()
plt.figure()
raw_data[raw_data['Produk'] == 'C'].hist()
plt.tight_layout()
plt.show()
plt.figure()
raw_data[raw_data['Produk'] == 'D'].hist()
plt.tight_layout()
plt.show()
plt.figure()
raw_data[raw_data['Produk'] == 'E'].hist()
plt.tight_layout()
plt.show()

# =====  Hex Bin Plot  =====
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
plt.clf()
plt.figure()
raw_data.plot.hexbin(x='Pendapatan', y='Total', gridsize=25, rot=90)
plt.tight_layout()
plt.show()

# =====  Scatter Matrix Plot  =====
from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
plt.clf()
_, ax = plt.subplots(1, 1, figsize=(10,10))
scatter_matrix(raw_data, ax=ax)
plt.show()

# =====  Quiz  =====
from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
plt.clf()
_, ax = plt.subplots(1, 1, figsize=(10,10))
scatter_matrix(raw_data, diagonal='kde', ax=ax)
plt.show()
