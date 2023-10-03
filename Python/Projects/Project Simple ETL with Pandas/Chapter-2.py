# =====  Extract  =====
import pandas as pd
df_participant = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqthon-participants.csv')

# =====  Transform Bagian I - Kode Pos  =====
df_participant['postal_code'] = df_participant['address'].str.extract(r'(\d+)$') #Masukkan regex Anda didalam fungsi extract

# =====  Transform Bagian II - Kota  =====
#Masukkan regex Anda didalam fungsi extract
df_participant['city'] = df_participant['address'].str.extract(r'(?<=\n)(\w.+)(?=,)')

# =====  Transform Bagian III - Github  =====
df_participant['github_profile'] = 'https://github.com/' + df_participant['first_name'].str.lower() + df_participant['last_name'].str.lower()

# =====  Transform Bagian IV - Nomor Handphone  =====
#Masukkan regex anda pada parameter pertama dari fungsi replace
df_participant['cleaned_phone_number'] = df_participant['phone_number'].str.replace(r'(\+62|62)', '0')
df_participant['cleaned_phone_number'] = df_participant['cleaned_phone_number'].str.replace(r'[()-]', '')
df_participant['cleaned_phone_number'] = df_participant['cleaned_phone_number'].str.replace(r'\s+', '')

# =====  Transform Bagian V - Nama Tim  =====
def func(col):
    abbrev_name = "%s%s"%(col['first_name'][0],col['last_name'][0]) #Singkatan dari Nama Depan dan Nama Belakang dengan mengambil huruf pertama
    country = col['country']
    abbrev_institute = '%s'%(''.join(list(map(lambda word: word[0], col['institute'].split())))) #Singkatan dari value di kolom institute
    return "%s-%s-%s"%(abbrev_name,country,abbrev_institute)
df_participant['team_name'] = df_participant.apply(func, axis=1)

# =====  Transform Bagian VI - Email  =====
def func(col):
    first_name_lower = col['first_name'].lower()
    last_name_lower = col['last_name'].lower()
    institute = ''.join(list(map(lambda word: word[0], col['institute'].lower().split()))) #Singkatan dari nama perusahaan dalam lowercase
    if 'Universitas' in col['institute']:
        if len(col['country'].split()) > 1: #Kondisi untuk mengecek apakah jumlah kata dari country lebih dari 1
            country = ''.join(list(map(lambda word: word[0], col['country'].lower().split())))
        else:
            country = col['country'][:3].lower()
        return "%s%s@%s.ac.%s"%(first_name_lower,last_name_lower,institute,country)
    return "%s%s@%s.com"%(first_name_lower,last_name_lower,institute)
df_participant['email'] = df_participant.apply(func, axis=1)

# =====  Transform Bagian VII - Tanggal Lahir  =====
df_participant['birth_date'] = pd.to_datetime(df_participant['birth_date'], format='%d %b %Y')

# =====  Transform Bagian VII - Tanggal Daftar Kompetisi  =====
df_participant['register_at'] = pd.to_datetime(df_participant['register_time'], unit='s')
