# =====  while  =====
#nilai awal j =0
j = 0 
#ketika j kurang dari 6 lakukan perulangan, jika tidak stop perulangan
while j<6: 
    #lakukan perintah ini ketika perulangan
    print("Ini adalah perulangan ke -",j) 
    #setiap kali diakhir perulangan update nilai dengan ditambah 1.
    j=j+1

# =====  for (1)  =====
#perulangan for sebagai inisialisasi dari angka 1 hingga angka yang lebih kecil daripada 6.
for i in range (1,6): 
    print("Ini adalah perulangan ke -", i) #perintah jika looping akan tetap berjalan

# =====  for (2) with access element  =====
for i in range (1,11):
    if(i%2==0):
        print("Angka genap",i)
    else:
         print("Angka ganjil",i)
