#Masukkan regex Anda didalam fungsi extract
df_participant['city'] = df_participant['address'].str.extract(r'(?<=\n)(\w.+)(?=,)') 
