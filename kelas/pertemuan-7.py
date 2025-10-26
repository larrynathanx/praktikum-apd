def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

print("Luas persegi :", luas_persegi(8))

def volume_persegi(sisi):
    volume = luas_persegi(sisi)*sisi
    return volume

print("Volume persegi: ", volume_persegi(8))

Nama = "Hambali"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# membuat variabel lokal
def info():
    Nama = "Informatika"
    Mata_Kuliah = "Logika Informatika"

# mengakses variabel lokal
    print("Prodi:", Nama)
    print("Mata Kuliah:", Mata_Kuliah)

# mengakses variabel global
print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

# memanggil fungsi info
info()

def faktorial(n):
# Basis (Base Case): Kondisi berhenti
    if n == 1 or n == 0:
        return 1
# Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
    else:
        return n * faktorial(n - 1)
# Memanggil fungsi
hasil = faktorial(5)
print(f"Hasil dari 5! adalah: {hasil}")

# Fungsi untuk menampilkan semua data
Film = []
def show_data():
    if len(Film) <= 0:
        print("Belum Ada data")
    else:
        print("ID | Judul Film")
    for indeks in range(len(Film)):
        print(indeks, "|", Film[indeks])
show_data() 

angka = int(input('Masukkan Angka : '))
print(angka) #input 'Hai'
try:
    angka = int(input('Masukkan Angka : '))
except ValueError:
    print('input yang anda masukkan bukan Integer (angka)')
else :
    print(f'Angka yang kamu input : {angka}') 