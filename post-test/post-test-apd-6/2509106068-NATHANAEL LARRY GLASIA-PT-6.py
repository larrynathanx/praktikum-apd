import os

daftar_bibit = {
    "bibit1" : {"nama": "Mangga Arumanis", "jenis": "Buah", "harga": 75000, "stok": 5},
    "bibit2" : {"nama": "Durian Montong", "jenis": "Buah", "harga": 120000, "stok": 3},
    "bibit3" : {"nama": "Mangga Gadung", "jenis": "Buah", "harga": 80000, "stok": 4},
    "bibit4" : {"nama": "Ketapang Kencana", "jenis": "Pohon", "harga": 27000, "stok": 12},
    "bibit5" : {"nama": "Cemara Norfolk", "jenis": "Pohon", "harga": 35000, "stok": 11},
    "bibit6" : {"nama": "Pucuk Merah", "jenis": "Hias", "harga": 25000, "stok": 10},
    "bibit7" : {"nama": "Anting Putri", "jenis": "Hias", "harga": 150000, "stok": 8},
    "bibit8" : {"nama": "Durian Lai", "jenis": "Buah", "harga": 65000, "stok": 4}
}

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "nathan": {"password": "0099", "role": "user"}
}

while True:
    os.system('cls')
    print("="*45)
    print("SELAMAT DATANG DI ANEKA BIBIT".center(45))
    print("="*45)
    print("1. Register Pengguna Baru")
    print("2. Login")
    print("3. Keluar")
    print("="*45)

    menu_awal = input("Pilih menu (1/2/3): ")

    if menu_awal == "1":
        os.system('cls')
        print("="*45)
        print("REGISTER PENGGUNA BARU".center(45))
        print("="*45)
        user_baru = input("Masukkan username baru: ")
        if user_baru in users:
            print("Username sudah terdaftar. Silakan coba lagi.")
        else:
            pw_baru = input("Masukkan password baru: ")
            users[user_baru] = {"password": pw_baru, "role": "user"}
            print(f"Akun dengan username '{user_baru}' berhasil dibuat!")
        input("Tekan ENTER untuk kembali...")

    elif menu_awal == "2":
        os.system('cls')
        print("="*45)   
        print("=== Login ===".center(45))
        print("="*45)
        username = input("Username: ")
        password = input("Password: ")
        if username in users and password == users[username]["password"]:
            role = users[username]["role"]
            print(f"\nLogin berhasil sebagai {role}!")
            input("\nTekan ENTER untuk lanjut...")
            if role == "admin":
                while True:
                    os.system('cls')
                    print("="*45)
                    print("MENU ADMIN - ANEKA BIBIT".center(45))
                    print("="*45)
                    print("1. Lihat Data Bibit")
                    print("2. Tambah Data Bibit")
                    print("3. Ubah Data Bibit")
                    print("4. Hapus Data Bibit")
                    print("5. Keluar")
                    print("="*45)
                    pilihan_admin = input("Pilih menu (1-5): ")

                    if pilihan_admin == "1":
                        os.system('cls')
                        print("=== DAFTAR BIBIT TANAMAN ===\n")
                        for bibit, data in daftar_bibit.items():
                            print(f"{bibit}: {data}")
                        input("\nTekan ENTER untuk kembali...")

                    elif pilihan_admin == "2":
                        os.system('cls')
                        print("=== TAMBAH DATA BIBIT ===\n")
                        kode_bibit = input("Masukkan kode bibit baru: ")
                        if kode_bibit in daftar_bibit:
                            print("Kode bibit sudah ada. Silakan coba lagi.")
                        else:
                            nama_baru = input("Nama Bibit: ")
                            jenis_baru = input("Jenis Bibit: ")
                            harga_baru = int(input("Harga Bibit: "))
                            stok_baru = int(input("Stok Bibit: "))
                            daftar_bibit[kode_bibit] = {"nama": nama_baru, "jenis": jenis_baru, "harga": harga_baru, "stok": stok_baru}
                            print(f"Bibit '{nama_baru}' berhasil ditambahkan!")
                        input("Tekan ENTER untuk kembali...")

                    elif pilihan_admin == "3":
                        os.system('cls')
                        print("=== UBAH DATA BIBIT ===\n")
                        kode_bibit = input("Masukkan kode bibit yang akan diubah: ")
                        if kode_bibit in daftar_bibit:
                            nama_baru = input("Nama Bibit Baru: ")
                            jenis_baru = input("Jenis Bibit Baru: ")
                            harga_baru = int(input("Harga Bibit Baru: "))
                            stok_baru = int(input("Stok Bibit Baru: "))
                            daftar_bibit[kode_bibit] = {"nama": nama_baru, "jenis": jenis_baru, "harga": harga_baru, "stok": stok_baru}
                            print(f"Bibit dengan kode '{kode_bibit}' berhasil diubah!")
                        else:
                            print("Kode bibit tidak valid")
                            input("\nTekan ENTER untuk kembali...")
                    
                    elif pilihan_admin == "4":
                        os.system('cls')
                        print("=== HAPUS DATA BIBIT ===\n")
                        kode_hapus_bibit = input("Masukkan kode bibit yang akan dihapus: ")
                        if kode_hapus_bibit in daftar_bibit:
                            del daftar_bibit[kode_hapus_bibit]
                            print(f"Bibit dengan kode '{kode_hapus_bibit}' berhasil dihapus!")
                        else:
                            print("Kode bibit tidak valid")
                            input("\nTekan ENTER untuk kembali...")

                    elif pilihan_admin == "5":
                        os.system('cls')
                        print("Keluar dari menu admin Aneka Bibit...")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")
                        input("\nTekan ENTER untuk kembali...")

            elif role == "user":
                while True:
                    os.system('cls')
                    print("="*45)
                    print("MENU USER - ANEKA BIBIT".center(45))
                    print("="*45)
                    print("1. Lihat Data Bibit")
                    print("2. Beli Bibit")
                    print("3. Keluar")
                    print("="*45)
                    pilihan_user = input("Pilih menu (1-3): ")

                    if pilihan_user == "1":
                        os.system('cls')
                        print("=== DAFTAR BIBIT TANAMAN ===\n")
                        for bibit, data in daftar_bibit.items():
                            print(f"{bibit}: {data}")
                        input("\nTekan ENTER untuk kembali...")

                    elif pilihan_user == "2":
                        os.system('cls')
                        print("=== BELI BIBIT ===\n")
                        print("Daftar Bibit yang Tersedia:\n")
                        for bibit, data in daftar_bibit.items():
                            print(f"{bibit}: {data}")
                        kode_beli_bibit = input("\nMasukkan kode bibit yang akan dibeli: ")
                        if kode_beli_bibit in daftar_bibit:
                            jumlah_beli = int(input("\nMasukkan jumlah yang akan dibeli: "))
                            if jumlah_beli <= daftar_bibit[kode_beli_bibit]["stok"]:
                                total = jumlah_beli*daftar_bibit[kode_beli_bibit]["harga"]
                                daftar_bibit[kode_beli_bibit]["stok"] -= jumlah_beli
                                print(f"\nAnda telah membeli {jumlah_beli} bibit '{daftar_bibit[kode_beli_bibit]['nama']}' dengan total harga Rp{total}.")
                                input("\nTekan ENTER untuk kembali...")
                            else:
                                print("\nStok tidak mencukupi!")
                        else:
                            print("Kode bibit tidak valid")
                            input("\nTekan ENTER untuk kembali...")

                    elif pilihan_user == "3":
                        os.system('cls')
                        print("Keluar dari menu user Aneka Bibit...")
                        break

                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")
                        input("\nTekan ENTER untuk kembali...")
        else:
            print("\nUsername atau password Anda salah!")
            input("\nTekan ENTER untuk kembali...")

    elif menu_awal == "3":
        os.system('cls')
        print("="*45)
        print("\nTerimakasih sudah menggunakan aplikasi Aneka Bibit!\n".center(45))
        print("="*45)
        break
    else:
        print("\nPilihan tidak valid.")
        input("\nTekan ENTER untuk mengulang...")