#Masukkan regex Anda didalam fungsi extract
df_participant['postal_code'] = df_participant['address'].str.extract(r'(\d+)$') 
