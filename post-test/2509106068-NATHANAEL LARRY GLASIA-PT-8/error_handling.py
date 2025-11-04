def input_int(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi")

def validasi_input(kode, daftar_bibit):
    if kode not in daftar_bibit:
        print("Kode bibit tidak ditemukan")
        input("\nTekan ENTER untuk mengulang...")
        kode_baru = input("Masukkan kode bibit yang valid: ")
        return validasi_input(kode_baru, daftar_bibit)
    return True