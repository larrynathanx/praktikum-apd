#DICTIONARY

daftar_buku = {
    "Buku1" : "Bumi Manusia",
    "Buku2" : "Laut Bercerita"
}
print(daftar_buku["Buku2"])
print(daftar_buku)

Biodata = {
    "Nama"  : "Nathanael Larry Glasia",
    "Umur"  : 18,
    "NIM"   : 2509106068,
    "KRS"   : ["Pemrograman Web", "Struktur Data", "Basis Data"],
    "Mahasiswa Aktif"   : True,
    "Sosmed"    : {
        "Instagram"  : "nthnllrry"
    }
}

print(f"nama saya adalah {Biodata["Nama"]}")
print(f"Instagram : {Biodata['Sosmed']['Instagram']}")
print(f"nama saya adalah {Biodata.get['Nama']}")
print(Biodata.get("Nama"))

Nilai = {
"Matematika": 80,
"B. Indonesia": 90,
"B. Inggris": 81,
"Kimia": 78,
"Fisika": 80
}
# Tanpa menggunakan items()
for i in Nilai:
    print(i)
print("") # pemisah
# Menggunakan items()
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")