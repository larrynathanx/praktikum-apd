import os

daftar_bibit = {
    "bibit1" : {"nama": "Mangga Arumanis", "jenis": "Buah", "harga": 75000, "stok": 500},
    "bibit2" : {"nama": "Durian Montong", "jenis": "Buah", "harga": 120000, "stok": 500},
    "bibit3" : {"nama": "Mangga Gadung", "jenis": "Buah", "harga": 80000, "stok": 500},
    "bibit4" : {"nama": "Ketapang", "jenis": "Pohon", "harga": 165000, "stok": 500},
    "bibit5" : {"nama": "Cemara Norfolk", "jenis": "Pohon", "harga": 35000, "stok": 500},
    "bibit6" : {"nama": "Pucuk Merah", "jenis": "Hias", "harga": 25000, "stok": 500},
    "bibit7" : {"nama": "Anting Putri", "jenis": "Hias", "harga": 150000, "stok": 500},
    "bibit8" : {"nama": "Durian Lai", "jenis": "Buah", "harga": 65000, "stok": 500}
}

users = {
    "admin" : {"password": "admin123", "role": "admin"},
    "nathan" : {"password": "gakjago", "role": "user"}
}

logged_in_user = None

def tampilkan_judul():
    print("="*45)
    print("SELAMAT DATANG DI ANEKA BIBIT".center(45))
    print("="*45)

def tampilkan_menu_admin():
    print("="*45)
    print("MENU ADMIN - ANEKA BIBIT".center(45))
    print("="*45)
    print("1. Lihat Daftar Bibit")
    print("2. Tambah Bibit Baru")
    print("3. Ubah Data Bibit")
    print("4. Hapus Data Bibit")
    print("5. Hitung Total Stok")
    print("6. Keluar")
    print("="*45)

def tampilkan_menu_user():
    print("="*45)
    print("MENU USER - ANEKA BIBIT".center(45))
    print("="*45)
    print("1. Lihat Daftar Bibit")
    print("2. Beli Bibit")
    print("3. Keluar")
    print("="*45)

def hitung_jumlah_bibit():
    return len(daftar_bibit)

def hitung_total(harga, jumlah):
    return harga*jumlah

def cek_login_user(username, password):
    return username in users and password == users[username]["password"]

def tampilkan_daftar_bibit():
    print("\nDaftar Bibit Tersedia:\n")
    print("Kode\tNama Bibit\tJenis\tHarga\tStok")
    print("-"*45)
    for kode_bibit, data in daftar_bibit.items():
        print(f"{kode_bibit}\t{data['nama']}\t{data['jenis']}\t{data['harga']}\t{data['stok']}")

def update_stok(kode_bibit, jumlah):
    daftar_bibit[kode_bibit]["stok"] -= jumlah

def hitung_total_stok(bibit, keys = None, i= 0):
    if keys is None:
        keys = list(bibit.keys())
    if i >= len(keys):
        return 0
    kode_bibit = keys[i]
    return bibit[kode_bibit]["stok"] + hitung_total_stok(bibit, keys, i + 1)

while True:
    os.system("cls || clear")
    tampilkan_judul()
    print("1. Register Pengguna Baru")
    print("2. Login")
    print("3. Keluar")
    print("="*45)

    menu_awal = input("Pilih menu (1/2/3): ")

    if menu_awal == "1":
        os.system("cls || clear")
        print("REGISTER PENGGUNA BARU".center(45))
        print("="*45)
        user_baru = input("Masukkan username baru: ")
        if user_baru in users:
            print("Username sudah ada, coba nama lain")
        else:
            pw_baru = input("Masukkan password baru: ")
            users[user_baru] = {"password": pw_baru, "role": "user"}
            print(f"Akun dengan username {user_baru} berhasil dibuat!")
        input("Tekan ENTER untuk kembali...")

    elif menu_awal == "2":
        os.system("cls || clear")
        print("LOGIN".center(45))
        print("="*45)
        username = input("Username: ")
        password = input("Password: ")

        if cek_login_user(username, password):
            role = users[username]["role"]
            logged_in_user = username
            print(f"\nLogin berhasil sebagai {role}!")
            input("\nTekan ENTER untuk melanjutkan...")

            if role == "admin":
                while True:
                    os.system("cls || clear")
                    tampilkan_menu_admin()
                    pilihan_admin = input("Pilih menu (1-5): ")

                    if pilihan_admin == "1":
                        os.system("cls || clear")
                        tampilkan_daftar_bibit()
                        input("\nTekan ENTER untuk kembali...")
                    
                    elif pilihan_admin == "2":
                        os.system("cls || clear")
                        print("TAMBAH DATA BIBIT\n")
                        kode_bibit = input("Masukkan kode bibit baru: ")

                        if kode_bibit in daftar_bibit:
                            print("Kode bibit sudah ada")
                        else:
                            try:
                                nama_baru = input("Nama bibit baru: ")
                                jenis_baru = input("Jenis bibit baru: ")
                                harga_baru = int(input("Masukkan harga bibit baru: "))
                                stok_baru = int(input("Masukkan stok bibit baru: "))
                                daftar_bibit[kode_bibit] = {"nama": nama_baru, "jenis": jenis_baru, "harga": harga_baru, "stok": stok_baru}
                                print("Bibit berhasil ditambahkan")
                            except ValueError:
                                print("Harga dan stok harus angka!!!")
                        input("Tekan ENTER untuk kembali...")

                    elif pilihan_admin == "3":
                        os.system("cls || clear")
                        print("UBAH DATA BIBIT\n")
                        kode_bibit = input("Masukkan kode bibit: ")

                        if kode_bibit in daftar_bibit:
                            try:
                                nama_baru = input("Nama bibit baru: ")
                                jenis_baru = input("Jenis bibit baru: ")
                                harga_baru = int(input("Masukkan harga bibit baru: "))
                                stok_baru = int(input("Masukkan stok bibit baru: "))
                                daftar_bibit[kode_bibit] = {"nama": nama_baru, "jenis": jenis_baru, "harga": harga_baru, "stok": stok_baru}
                                print("Data berhasil diubah") 
                            except ValueError:
                                print("Input harus berupa angka")
                        else:
                            print("Kode tidak valid")
                        input("\nTekan ENTER untuk kembali...")

                    elif pilihan_admin == "4":
                        os.system("cls || clear")
                        print("HAPUS DATA BIBIT\n")
                        
                        kode_hapus = input("Masukkan data bibit yang ingin dihapus: ")

                        if kode_hapus in daftar_bibit:
                            del daftar_bibit[kode_hapus]
                            print("Data berhasil dihapus!")
                        else:
                            print("Kode tidak valid")
                        input("\nTekan ENTER untuk kembali...")
                    
                    elif pilihan_admin == "5":
                        os.system("cls || clear")
                        print("TOTAL STOK BIBIT\n")
                        total_stok = hitung_total_stok(daftar_bibit) 
                        print(f"Total stok bibit yang tersedia di Aneka Bibit: {total_stok} bibit")
                        input("\nTekan ENTER untuk kembali...")

                    elif pilihan_admin == "6":
                        break

                    else:
                        print("Pilihan tidak valid")
                        input("\nTekan ENTER untuk kembali...")

            elif role == "user":
                while True:
                    os.system("cls || clear")
                    tampilkan_menu_user()
                    pilihan_user = input("Pilih menu (1-3): ")

                    if pilihan_user == "1":
                        os.system("cls || clear")
                        tampilkan_daftar_bibit()
                        input("\nTekan ENTER untuk kembali... ")
                    
                    elif pilihan_user == "2":
                        os.system("cls || clear")
                        tampilkan_daftar_bibit()
                        kode_beli = input("\nMasukkan kode bibit yang ingin dibeli: ")

                        if kode_beli in daftar_bibit:
                            try:
                                jumlah = int(input("Jumlah beli: "))
                                if jumlah <= 0: 
                                    print("Harus lebih dari 0!")

                                elif jumlah <= daftar_bibit[kode_beli]["stok"]:
                                    total = hitung_total(daftar_bibit[kode_beli]["harga"], jumlah)
                                    update_stok(kode_beli, jumlah)
                                    print(f"\nAnda membeli {jumlah} {daftar_bibit[kode_beli]["nama"]} dengan total harga Rp{total}")
                                else:
                                    print("Stok tidak mencukupi")
                            except ValueError:
                                print("Jumlah harus angka")
                        else:
                            print("Kode tidak valid")
                        input("\nTekan ENTER untuk kembali...")

                    elif pilihan_user == "3":
                        break
                    else:
                        print("Pilihan tidak valid")
                        input("\nTekan ENTER untuk kembali...")

        else:
            print("Username atau Password salah")
            input("\nTekan ENTER untuk kembali")

    elif menu_awal == "3":
        os.system("cls || clear")
        print("\nTERIMAKASIH TELAH MENGGUNAKAN ANEKA BIBIT!\n")
        break

    else:
        print("\nPilihan tidak valid")
        input("\nTekan ENTER untuk menginput ulang pilihan...")






