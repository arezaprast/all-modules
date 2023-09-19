# =====  Read Dataset CSV dan TSV  =====
import pandas as pd
# File CSV
df_csv = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/sample_csv.csv')
print(df_csv.head(3)) # Menampilkan 3 data teratas
# File TSV
df_tsv = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv', sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas

# =====  Read Dataset Excel  =====
import pandas as pd
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx', sheet_name='test')
print(df_excel.head(4)) # Menampilkan 4 data teratas

# =====  Read Dataset JSON  =====
import pandas as pd
# File JSON
url = 'https://storage.googleapis.com/dqlab-dataset/covid2019-api-herokuapp-v2.json'
df_json = pd.read_json(url)
print(df_json.head(10)) # Menampilkan 10 data teratas

# =====  Head & Tail  =====
import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/sample_csv.csv')
# Tampilkan 3 data teratas
print("Tiga data teratas:\n", df.head(3))
# Tampilkan 3 data terbawah
print("Tiga data terbawah:\n", df.tail(3))
