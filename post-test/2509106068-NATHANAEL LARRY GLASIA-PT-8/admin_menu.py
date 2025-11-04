import os
import inquirer
from prettytable import PrettyTable
from error_handling import input_int, validasi_input

def tampilkan_bibit(daftar_bibit):
    os.system('cls || clear')
    tabel = PrettyTable(["Kode", "Nama", "Jenis", "Harga", "Stok"])
    for kode, data in daftar_bibit.items():
        tabel.add_row([kode, data["nama"], data["jenis"], data["harga"], data["stok"]])
    print(tabel)
    input("\nTekan ENTER untuk kembali...")

def tambah_bibit(daftar_bibit):
    os.system('cls || clear')
    print("="*45)
    print("=== TAMBAH DATA BIBIT ===".center(45))
    print("="*45)
    kode = input("Masukkan kode bibit baru: ")
    if kode in daftar_bibit:
        print("Kode bibit sudah ada")
    else:
        nama = input("Nama bibit: ")
        jenis = input("Jenis bibit: ")
        harga = input_int("Harga: ")
        stok = input_int("Stok: ")
        if harga is not None and stok is not None:
            daftar_bibit[kode] = {"nama": nama, "jenis": jenis, "harga": harga, "stok": stok}
            print(f"Bibit '{nama}' berhasil ditambahkan!")
        input("\nTekan ENTER untuk kembali...")

def ubah_bibit(daftar_bibit):
    os.system('cls || clear')
    print("="*45)
    print("=== UBAH DATA BIBIT ===".center(45))
    print("="*45)
    kode = input("Masukkan kode bibit yang akan diubah: ")
    if validasi_input(kode, daftar_bibit):
        nama = input("Nama baru: ")
        jenis = input("Jenis: ")
        harga = input_int("Harga: ")
        stok = input_int("Stok: ")
        if harga is not None and stok is not None:
            daftar_bibit[kode] = {"nama": nama, "jenis": jenis, "harga": harga, "stok": stok}
            print("Data berhasil diperbarui!")
        input("\nTekan ENTER untuk kembali...")

def hapus_bibit(daftar_bibit):
    os.system('cls || clear')
    print("="*45)
    print("=== HAPUS DATA BIBIT ===".center(45))
    print("="*45)
    kode = input("Masukkan kode bibit yang akan dihapus: ")
    if validasi_input(kode, daftar_bibit):
        del daftar_bibit[kode]
        print("Data berhasil dihapus!")
    input("\nTekan ENTER untuk kembali...")

def total_stok(daftar_bibit):
    os.system('cls || clear')
    total = sum(data["stok"] for data in daftar_bibit.values())
    print(f"Total stok bibit yang ada di Aneka Bibit: {total} bibit.")
    input("\nTekan ENTER untuk kembali...")

def menu_admin(daftar_bibit):
    while True:
        os.system('cls || clear')
        pilihan = [
            inquirer.List(
                "pilih",
                message = "Pilih menu Admin",
                choices = [
                    "1. Lihat Data Bibit",
                    "2. Tambah Data Bibit",
                    "3. Ubah Data Bibit",
                    "4. Hapus Data Bibit",
                    "5. Hitung Total Stok Bibit Sekarang",
                    "6. Kembali"
                ]
            )
        ]
        pilihan_jawaban = inquirer.prompt(pilihan)["pilih"]

        if pilihan_jawaban.startswith("1"):
            tampilkan_bibit(daftar_bibit)
        elif pilihan_jawaban.startswith("2"):
            tambah_bibit(daftar_bibit)
        elif pilihan_jawaban.startswith("3"):
            ubah_bibit(daftar_bibit)
        elif pilihan_jawaban.startswith("4"):
            hapus_bibit(daftar_bibit)
        elif pilihan_jawaban.startswith("5"):
            total_stok(daftar_bibit)
        elif pilihan_jawaban.startswith("6"):
            break