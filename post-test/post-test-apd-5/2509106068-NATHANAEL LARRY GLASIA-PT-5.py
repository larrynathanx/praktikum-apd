import os


daftar_bibit = [
    ["Mangga Arumanis", "Buah", 75000, 5],
    ["Durian Monthong", "Buah", 70000, 10],
    ["Mangga Gadung", "Buah", 75000, 25],
    ["Ketapang Kencana", "Pohon", 27000, 12],
    ["Cemara Norfolk", "Pohon", 35000, 11],
    ["Pucuk Merah", "Hias", 25000, 10],
    ["Anting Putri", "Hias", 150000, 8],
    ["Durian Lai", "Buah", 65000, 4]
]

users = [
    ["bobotbibit", "1993", "admin"],
    ["nathan", "0099", "user"]
]

pengguna_new = []

while True:
    os.system('cls')
    print("="*50)
    print("SELAMAT DATANG DI ANEKA BIBIT".center(50))
    input("\nTekan ENTER untuk lanjut...")
    os.system('cls')

    print("="*50)
    print("LOGIN SEBAGAI:".center(50))
    print("="*50)
    print("1. Admin")
    print("2. Pengguna Biasa")
    print("3. Pengguna Baru")
    print("="*50)
    menu_awal = input("\nPilih menu (1/2/3): ")

    
    if menu_awal == "1":
        os.system('cls')
        print("="*50)
        print("LOGIN SEBAGAI ADMIN".center(50))
        print("="*50)
        username = input("\nUsername: ")
        pw = input("Password: ")

        if username == users[0][0] and pw == users[0][1]:
            print("\nBerhasil login sebagai Admin!")
            input("Tekan ENTER untuk lanjut...")
            
            while True:
                os.system('cls')
                print("="*50)
                print("MENU ADMIN - ANEKA BIBIT".center(50))
                print("="*50)
                print("""
                        1. Lihat Data Bibit
                        2. Tambah Data Bibit
                        3. Ubah Data Bibit
                        4. Hapus Data Bibit
                        5. Keluar
                    """)
                print("="*50)
                pilihan_admin = input("Pilih menu (1-5): ")

                if pilihan_admin == "1":
                    os.system('cls')
                    print("=== DAFTAR BIBIT TANAMAN ===\n")
                    for i in range(len(daftar_bibit)):
                        print(f"{i+1}. {daftar_bibit[i]}")
                    input("\nTekan ENTER untuk kembali...")

                elif pilihan_admin == "2":
                    os.system('cls')
                    print("=== TAMBAH DATA BIBIT ===\n")
                    nama = input("Nama bibit: ")
                    jenis = input("Jenis (Buah/Hias/Pohon): ")
                    harga = input("Harga bibit: ")
                    stok = input("Stok: ")

                    if not harga.isdigit() or not stok.isdigit():
                        print("\nHarga dan stok harus berupa angka!")
                    else:
                        daftar_bibit.append([nama, jenis, int(harga), int(stok)])
                        print("\nData bibit berhasil ditambahkan!")
                    input("\nTekan ENTER untuk kembali...")

                elif pilihan_admin == "3":
                    os.system('cls')
                    print("=== UBAH DATA BIBIT ===\n")
                    for i in range (len(daftar_bibit)):
                        print(f"{i+1}. {daftar_bibit[i]}")

                    edit_bibit = input("\nMasukkan nomor bibit yang ingin diubah: ")
                    if edit_bibit.isdigit():
                        idx = int(edit_bibit) - 1
                        if 0 <= idx < len(daftar_bibit):
                            nama_baru = input("Nama baru: ")
                            jenis_baru = input("Jenis baru: ")
                            harga_baru = input("Harga baru: ")
                            stok_baru = input("Stok baru: ")

                            if harga_baru.isdigit():
                                daftar_bibit[idx][2] = int(harga_baru)
                            if stok_baru.isdigit():
                                daftar_bibit[idx][3] = int(stok_baru)

                            daftar_bibit[idx][0] = nama_baru
                            daftar_bibit[idx][1] = jenis_baru
                            print("\nData bibit berhasil diperbarui!")
                        else:
                            print("\nNomor bibit tidak valid!")
                    else:
                        print("\nInput harus berupa angka!")
                    input("\nTekan ENTER untuk kembali...")

                elif pilihan_admin == "4":
                    os.system('cls')
                    print("=== HAPUS DATA BIBIT ===\n")
                    for i in range(len(daftar_bibit)):
                        print(f"{i+1}. {daftar_bibit[i]}")

                    hapus_bibit = input("\nMasukkan nomor bibit yang ingin dihapus: ")
                    if hapus_bibit.isdigit():
                        hapus_bibit = int(hapus_bibit)
                        if 1 <= hapus_bibit <= len(daftar_bibit):
                            hapus_nama = daftar_bibit.pop(hapus_bibit - 1)
                            print(f"\nBibit '{hapus_nama[0]}' berhasil dihapus!")
                        else:
                            print("\nNomor bibit tidak valid!")
                    else:
                        print("\nInput harus angka!")
                    input("\nTekan ENTER untuk kembali...")

                elif pilihan_admin == "5":
                    break
                else:
                    print("\nPilihan tidak valid!")
                    input("\nTekan ENTER untuk kembali...")

        else:
            print("\nUsername atau Password Admin salah!")
            input("\nTekan ENTER untuk kembali ke beranda...")
            

    elif menu_awal == "2":
        os.system('cls')
        print("="*50)
        print("LOGIN SEBAGAI PENGGUNA".center(50))
        print("="*50)
        user_biasa = input("\nUsername: ")
        pw_biasa = input("Password: ")

        if user_biasa == users[1][0] and pw_biasa == users[1][1]:
            print("\nBerhasil Login Sobat Bibit!")
            input("\nTekan ENTER untuk lanjut...")

            while True:
                os.system('cls')
                print("="*50)
                print("MENU PENGGUNA".center(50))
                print("="*50)
                print("""
                    1. Lihat Daftar Bibit
                    2. Beli Bibit
                    3. Keluar
                    """)
                pilihan_user = input("Pilih Menu (1/2/3): ")

                if pilihan_user == "1":
                    os.system('cls')
                    print("=== DAFTAR BIBIT TANAMAN ===")
                    for i in range (len(daftar_bibit)):
                        print(f"{i+1}. {daftar_bibit[i]}")
                    input("\nTekan ENTER untuk kembali...")

                elif pilihan_user == "2":
                    os.system('cls')
                    print("=== BELI BIBIT ===\n")
                    for i in range (len(daftar_bibit)):
                        print(f"{i+1}. {daftar_bibit[i]}")

                    nomor_beli = input("\nNomor bibit yang dibeli: ")
                    jumlah_beli = input("Jumlah yang dibeli: ")

                    if nomor_beli.isdigit() and jumlah_beli.isdigit():
                        nomor_beli = int(nomor_beli)
                        jumlah_beli = int(jumlah_beli)

                        if 1 <= nomor_beli <= len(daftar_bibit):
                            bibit = daftar_bibit[nomor_beli - 1]
                            if jumlah_beli <= bibit[3]:
                                total = bibit[2] * jumlah_beli
                                bibit[3] -= jumlah_beli
                                print(f"\nPembelian {jumlah_beli} bibit '{bibit[0]}' berhasil!")
                                print(f"Total harga: Rp{total}")
                                print("Terimakasih sudah membeli di Aneka Bibit!")
                            else:
                                print("\nStok tidak mencukupi!")
                        else:
                            print("\nNomor bibit tidak valid!")
                    else:
                        print("\nNomor dan jumlah harus berupa angka!")
                    input("\nTekan ENTER untuk kembali...")
                
                elif pilihan_user == "3":
                    input("\nTekan ENTER")
                    login_user = False
                    break
                else:
                    print("\nPilihan tidak valid!")
                    input("\nTekan ENTER untuk kembali...")
        else:
            print("\nUsername atau password salah!")
            input("\nTekan ENTER untuk kembali...")

    elif menu_awal == "3":
            os.system('cls')
            print("="*50)
            print("DAFTAR SEBAGAI PENGGUNA BARU".center(50))
            print("="*50)
            user_baru = input("\nUsername baru: ")
            pw_baru = input("Password baru: ")
            pengguna_new.append([user_baru])
            pengguna_new.append([pw_baru])
            print(f"\nPengguna {user_baru} berhasil terdaftar!")
            input("\nTekan ENTER untuk login...")
    else:
        print("\nPilihan tidak valid!")
        input("\nTekan ENTER untuk kembali ke beranda...")
        
    



