import os
import inquirer
from prettytable import PrettyTable
from error_handling import input_int, validasi_input

def tampilkan_bibit(daftar_bibit):
    os.system('cls || clear')
    print("="*45)
    print("=== DAFTAR BIBIT ===".center(45))
    print("="*45)
    tabel = PrettyTable(["Kode", "Nama", "Jenis", "Harga", "Stok"])
    for kode, data in daftar_bibit.items():
        tabel.add_row([kode, data["nama"], data["jenis"], data["harga"], data["stok"]])
    print(tabel)
    input("\nTekan ENTER untuk kembali...")

def beli_bibit(daftar_bibit):
    os.system('cls || clear')
    print("="*45)
    print("=== BELI BIBIT ===".center(45))
    print("="*45)
    tabel = PrettyTable(["Kode", "Nama", "Jenis", "Harga", "Stok"])
    for kode, data in daftar_bibit.items():
        tabel.add_row([kode, data["nama"], data["jenis"], data["harga"], data["stok"]])
    print(tabel)
    kode_beli = input("\nMasukkan kode bibit yang mau dibeli: ")
    kode_beli = validasi_input(kode_beli, daftar_bibit)

    jumlah = input_int("Jumlah beli: ")
    if jumlah is not None and jumlah <= daftar_bibit[kode_beli]["stok"]:
        total_beli = jumlah*daftar_bibit[kode_beli]["harga"]
        daftar_bibit[kode_beli]["stok"] -= jumlah
        print(f"\nBerhasil membeli {jumlah} bibit {daftar_bibit[kode_beli]['nama']}. Total pembelian: Rp{total_beli}.")
        input("\nTekan ENTER untuk kembali...")
    else:
        print("Stok tidak mencukupi")
        input("\nTekan ENTER untuk kembali...")

def menu_user(daftar_bibit):
    while True:
        os.system('cls || clear')
        pertanyaan = [
            inquirer.List(
                "pilih",
                message = "Pilih menu User",
                choices = [
                    "1. Lihat Data Bibit",
                    "2. Beli Bibit",
                    "3. Kembali"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)["pilih"]

        if jawaban.startswith("1"):
            tampilkan_bibit(daftar_bibit)
        elif jawaban.startswith("2"):
            beli_bibit(daftar_bibit)
        elif jawaban.startswith("3"):
            break