# =====  Import Package  =====
import matplotlib.pyplot as plt
import plotnine as p9
import pandas as pd
# =====  Baca Data  =====
import pandas as pd
df_penduduk = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv")
df_inflasi = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/inflasi.csv")

# [Chapter - 2]
# =====  Menampilkan Data  =====
print(df_penduduk.head())
# =====  Menjalankan Fungsi ggplot  =====
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')
ggplot(data=df_penduduk).draw()
plt.show()
# =====  Menambahkan Variabel  =====
(ggplot(data=df_penduduk)
+ aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
).draw()
plt.show()
# =====  Mendefinisikan Objek Geometris  =====
(ggplot(data=df_penduduk)
+ aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
+ geom_col()
).draw()
plt.show()
# =====  Membuat Horizontal Bar Chart  =====
(ggplot(data=df_penduduk)
+ aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
+ geom_col()
+ coord_flip()
).draw()
plt.tight_layout()
plt.show()
# =====  Menambah Judul dan Mengubah Label  =====
plotnine.options.figure_size=(12, 4.8)
(ggplot(data=df_penduduk)
+ aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
+ geom_col()
+ coord_flip()
+ labs(title='Jumlah penduduk per kabupaten/kota di DKI Jakarta(2013)',
x='Jumlah Penduduk',
y='Kabupaten/Kota')
).draw()
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()
# =====  Menampilkan Warna Berbeda  =====
plotnine.options.figure_size=(10, 3.6)
(ggplot(data=df_penduduk)
+ aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH', fill='JENIS KELAMIN')
+ geom_col()
+ coord_flip()
+ labs(title='Jumlah penduduk per kabupaten/kota di DKI Jakarta (2013)',
x='Jumlah Penduduk',
y='Kabupaten/Kota')
).draw()
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()
# =====  Membuat Grafik dengan Variabel Berbeda  =====
plotnine.options.figure_size=(14, 3.6)
(ggplot(data=df_penduduk[df_penduduk['NAMA KECAMATAN'] == 'CENGKARENG'])
+ aes(x='NAMA KELURAHAN', y='JUMLAH', fill='JENIS KELAMIN')
+ geom_col()
+ coord_flip()
+ labs(title='Jumlah penduduk per kelurahan di Kecamatan Cengkareng (2013)', x='Kelurahan', y='Jumlah Penduduk')
).draw()
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()
# =====  Memisahkan Grafik  =====
plotnine.options.figure_size=(10, 3.6)
(ggplot(data=df_penduduk[df_penduduk['NAMA KECAMATAN'] == 'CENGKARENG'])
+ aes(x='NAMA KELURAHAN', y='JUMLAH', fill='JENIS KELAMIN')
+ geom_col(position='position_dodge')
+ coord_flip()
+ labs(title='Jumlah penduduk per kelurahan di DKI Jakarta (2013)',
x='Kelurahan',
y='Jumlah Penduduk')
).draw()
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()

# [Chapter - 3]
# =====  Membuat Scatterplot  =====
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')
df_penduduk_luas_jumlah = df_penduduk.groupby(
  ['NAMA KELURAHAN', 'LUAS WILAYAH (KM2)'])['JUMLAH'].agg('sum').reset_index()
(ggplot(data=df_penduduk_luas_jumlah)
+ aes(x='LUAS WILAYAH (KM2)', y='JUMLAH')
+ geom_point()
).draw()
plt.show()
# =====  Memberi Warna pada Scatterplot  =====
import matplotlib.pyplot as plt
from plotnine import *
import plotnine
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')
df_penduduk_luas_jumlah = df_penduduk.groupby(
  ['NAMA KELURAHAN', 'LUAS WILAYAH (KM2)'])[['JUMLAH']].agg('sum').reset_index()
plotnine.options.figure_size=(10, 3.6)
(ggplot(data=df_penduduk_luas_jumlah)
+ aes(y='LUAS WILAYAH (KM2)', x='JUMLAH', color='JUMLAH')
+ geom_point()
).draw()
plt.show()
# =====  Membuat Histogram  =====
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')
(ggplot(data=df_penduduk)
+ aes(x='LUAS WILAYAH (KM2)')
+ geom_histogram()
).draw()
plt.show()
# =====  Membuat Histogram 2  =====
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')
(ggplot(data=df_penduduk)
+ aes(x='LUAS WILAYAH (KM2)', y='stat(count/max(count))')
+ geom_histogram()
).draw()
plt.show()
# =====  Membuat Boxplot  =====
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')
(ggplot(data=df_penduduk)
+ aes(x='NAMA KABUPATEN/KOTA', y='JUMLAH')
+ geom_boxplot()
+ coord_flip()
).draw()
plt.tight_layout()
plt.show()
# =====  Membuat Line Chart  =====
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_inflasi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/inflasi.csv')
df_inflasi['Bulan'] = pd.to_datetime(df_inflasi['Bulan'])
(ggplot(data=df_inflasi[df_inflasi['Negara']=='Indonesia'])
+ aes(x='Bulan', y='Inflasi')
+ geom_line()
).draw()
plt.show()
# =====  Membuat 2 Line Chart  =====
import matplotlib.pyplot as plt
from plotnine import *
import plotnine
import pandas as pd 
df_inflasi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/inflasi.csv')
df_inflasi['Bulan'] = df_inflasi['Bulan'].astype('datetime64')
plotnine.options.figure_size=(12, 3.6)
(ggplot(data=df_inflasi)
+ aes(x='Bulan', y='Inflasi', color='Negara')
+ geom_line()
).draw()
plt.show()
# =====  Mengubah Ukuran Plot  =====
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_inflasi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/inflasi.csv')
df_inflasi['Bulan'] = df_inflasi['Bulan'].astype('datetime64')
(ggplot(data=df_inflasi)
+ aes(x='Bulan', y='Inflasi', color='Negara')
+ geom_line()
+ theme(figure_size=(10, 5))
).draw()
plt.show()
