#mendefinisikan list
praktikum = ["Mahasiswa", 20, True, 45.10, ["APD", 25]]
print(praktikum) #menampilkan seluruh isi list

# menampilkan list
praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# memanggil satu elemen
print(praktikum[1])
# memanggil elemen di dalam list
print(praktikum[4][0])

# list awal
studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# Tambahkan Web
studyclub.append("Web")
print(studyclub)

# list awal
studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# Tambahkan Web
studyclub.insert(2,"Web")
print(studyclub)

# list awal
studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
print(studyclub)
# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
studyclub[2] = "AI"
print(studyclub)

# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# menghapus elemen pada indeks ke-2, yakni "Kalkulus"
del matakuliah[2]
print(matakuliah)

# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# menghapus elemen dengan nilai "Kalkulus"
matakuliah.remove('Kalkulus')
print(matakuliah)

# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
ambil_matkul = matakuliah.pop(2)
print(matakuliah)
print(ambil_matkul)

# list
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
'Orsikom','Basis Data']
# Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
print(matakuliah[1:6:2])

# List
a = [1, 2, 3]
b = [4, 5, 6]
# menggabungkan kedua list dengan operator (+)
c = a + b
print(c)

# List
a = ["teknik", "informatika"]
# mengulang isi list dengan operator (*) sebanyak 3 kali
c = a*3
print(c)

# Membuat Nested List
kelas = [
["Ridho", "Lian", "Nabil"],
["Daffa", "Dante", "Santoso"]
["Pernanda", "Riyadi", "Ahnaf"],
]
# Memanggil elemen "Santoso"
print(kelas[1][2])

# list mahasiswa
mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# perulangan for untuk mendapatkan semua elemen
for i in mahasiswa:
    for j in i :
        print (j)
# i dan j merupakan variabel sementara / temporary, kita dapat menggantinya dengan apa saja asal sesuai dengan syarat nama variabel.

#mendefinisikan tuple
anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
print(anggota) #menampilkan seluruh isi tuple

# menampilkan tuple
anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# memanggil satu elemen
print(anggota[1])
print(anggota[-1])

# memanggil elemen di dalam nested tuple
print(anggota[5][0])

# list awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
liststudy=list(studyclub)
# tuple awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# Ubah tuple menjadi list
liststudy=list(studyclub)
# Tambahkan Web
liststudy.append("Web")
# ubah kembali list menjadi tuple
studyclub=tuple(liststudy)
print(studyclub)

# tuple awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# Ubah tuple menjadi list
liststudy=list(studyclub)
# Tambahkan Web
liststudy.insert(2,"Web")
# ubah kembali list menjadi tuple
studyclub=tuple(liststudy)
print(studyclub)

# tuple awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
print(studyclub)
# Ubah tuple menjadi list
liststudy=list(studyclub)
# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
liststudy[2] = "AI"
# ubah kembali list menjadi tuple
studyclub=tuple(liststudy)
print(studyclub)

# tuple awal
hobi=("Futsal","Catur","Renang")
print(hobi)
# ubah tuple menjadi list
gemar=list(hobi)
# menghapus elemen pada indeks ke-2, yakni "Renang"
del gemar[2]
# Ubah list kembali menjadi tuple
hobi=tuple(gemar)
print(hobi)

# tuple awal
hobi=("Futsal","Catur","Renang")
print(hobi)
# ubah tuple menjadi list
gemar=list(hobi)
# menghapus elemen dengan nilai "catur"
gemar.remove("Catur")
# ubah list kembali menjadi tuple
hobi=tuple(gemar)
print(hobi)

# tuple awal
hobi=("Futsal","Catur","Renang")
print(hobi)
# ubah tuple menjadi list
gemar=list(hobi)
# Menghapus & mengambil elemen 'Futsal' pada indeks ke-2
hapus = gemar.pop(0)
# Ubah list kembali menjadi tuple
hobi=tuple(gemar)
print(hobi)
print(hapus)

# tuple
matakuliah = ('PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
'Orsikom','Basis Data')
# Menampilkan tuple mulai dari indeks 1 hingga 4 dengan loncatan 2
print(matakuliah[1:5:2])

# tuple
tugas = ('rangkuman', 'arduino','scrapping')
# beri variabel setiap values
(PTI, orsikom, basisdata) = tugas
print(PTI)
print(orsikom)
print(basisdata)

# tuple
barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# beri variabel setiap values
(segitiga, bulat, *kotak) = barang
print(segitiga)
print(bulat)
print(kotak)

# tuple
barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
angka=(1,2,3)
# simpan di dalam variabel baru
gabung=barang+angka
print(gabung)


