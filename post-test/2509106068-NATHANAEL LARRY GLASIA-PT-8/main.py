import os
import inquirer
from data_bibit import daftar_bibit
from list_users import users
from admin_menu import menu_admin
from user_menu import menu_user

while True:
    os.system('cls || clear')
    pertanyaan_awal = [
        inquirer.List(
            "menu awal",
            message = "SELAMAT DATANG DI ANEKA BIBIT!",
            choices = [ "1. Register",
                        "2. Login",
                        "3. Keluar"]
        )
    ]
    jawaban_awal = inquirer.prompt(pertanyaan_awal)["menu awal"]

    if jawaban_awal.startswith("1"):
        os.system('cls || clear')
        print("="*45)
        print("=== REGISTER ===".center(45))
        print("="*45)
        user_baru = input("Masukkan username baru Anda: ")
        if user_baru in users:
            print("Maaf, username sudah terdaftar. Masukkan nama username lain.")
            input("\nTekan ENTER untuk kembali")
        else:
            pw_baru = input("Masukkan password baru Anda: ")
            users[user_baru] = {"password": pw_baru, "role": "user"}
            print("Akun berhasil dibuat!")
            input("\nTekan ENTER untuk kembali...")

    elif jawaban_awal.startswith("2"):
        os.system('cls || clear')
        print("="*45)
        print("=== LOGIN ===".center(45))
        print("="*45)
        user = input("Username: ")
        pw = input("Password: ")
        if user in users and pw == users[user]["password"]:
            role = users[user]["role"]
            print(f"Login berhasil sebagai {role}!\n")
            input("Tekan ENTER untuk melanjutkan...")

            if role == "admin":
                menu_admin(daftar_bibit)
            else:
                menu_user(daftar_bibit)
        else:
            print("Username atau Password salah!")
            input("\nTekan ENTER untuk kembali...")

    elif jawaban_awal.startswith("3"):
        os.system('cls || clear')
        print("===== TERIMAKASIH SUDAH MENGGUNAKAN ANEKA BIBIT! SEMOGA HARI ANDA MENYENANGKAN! =====")
        break

