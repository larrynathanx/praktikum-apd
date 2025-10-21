nilai = 75

if nilai >= 70:
    print("Lulus") #Blok if dijalankan karena kondisi True
else:
    print("Tidak Lulus") #Blok else tidak dijalankan karena if terpenuhi

    # input nilai
umur = int(input("Masukkan umur Anda: "))
# misalnya, umur = 16
# Percabangan
if umur < 13:
    
    kategori = "Anak-anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"
# Menampilkan umur dan kategori
print("Umur:", umur, "Kategori:", kategori)
