username_input = str(input("Masukkan username Anda: "))
password_input = str(input("Masukkan password Anda: "))
username = "larry"
password = "068"


if username_input == username and password_input == password:
    print("Selamat datang di Kalkulator Multifungsi, Beta!")
else:
    if username_input != username and password_input != password:
        print("Username dan Password salah")
        exit()
    elif username_input != username:
        print("Username salah")
        exit()
    else:
        print("Password salah")
        exit()

print(" KALKULATOR MULTIFUNGSI ")
print("1. Konversi Panjang")
print("2. Konversi Massa")
print("3. Konversi Suhu")
print("4. Konversi Waktu")
print("5. Konversi Mata Uang")

pilihan = int(input("Masukkan pilihan: "))

if pilihan == 1:
        print("\n--- Konversi Panjang ---")
        print("1. kaki (feet) ke meter")
        print("2. kilometer ke meter")
        print("3. centimeter ke meter")
        sub = int(input("Pilih Konversi: "))
        
        if sub == 1:
            feet = float(input("Masukkan panjang (feet): "))
            print("Hasil:", feet*0.3048, "meter")
        elif sub == 2:
            kilometer = float(input("Masukkan panjang kilometer: "))
            print("Hasil:", kilometer*1000, "meter")
        elif sub == 3:
            centimeter = float(input("Masukkan panjang centimeter: "))
            print("Hasil:", centimeter/100, "meter" )
        else:
            print("Pilihan tidak tersedia")
            
elif pilihan == 2:
        print("\n--- Konversi Massa ---")
        print("1. pon (pound) ke kilogram")
        print("2. ton ke kilogram")
        print("3. gram ke kilogram")
        print("4. miligram ke kilogram")
        print("5. centigram ke kilogram")
        sub = int(input("Pilih konversi: "))

        if sub == 1:
            pound = float(input("Masukkan massa (pound): "))
            print("Hasil:", pound*0.454 , "kilogram")
        elif sub == 2:
            ton = float(input("Masukkan massa (ton): "))
            print("Hasil:", ton*1000, "kilogram")
        elif sub == 3:
            gram = float(input("Masukkan massa (gram): "))
            print("Hasil:", gram/1000, "kilogram")
        elif sub == 4:
            miligram = float(input("Masukkan massa (miligram): "))
            print("Hasil:", miligram/1000000, "kilogram")
        elif sub == 5:
            centigram = float(input("Masukkan massa (centigram): "))
            print("Hasil:", centigram/100000, "kilogram")
        else:
            print("Pilihan tidak tersedia")
            
elif pilihan == 3:
    print("\n--- Konversi Suhu ---")
    print("1. Celcius ke Kelvin")
    print("2. Fahrenheit ke Kelvin")
    print("3. Reamur ke Kelvin")
    sub = int(input("Pilih konversi: "))

    if sub == 1:
        celcius = float(input("Masukkan suhu (Celcius): "))
        print("Hasil:", celcius + 273.15, "K")
    elif sub == 2:
        fahrenheit = float(input("Masukkan suhu (Fahrenheit): "))
        print("Hasil:", 5/9*(fahrenheit - 32) + 273.15, "K")
    elif sub == 3:
        reamur = float(input("Masukkan suhu (Reamur): "))
        print("Hasil:", (5/4)*reamur + 273.15, "K")
    else:
        print("Pilihan tidak tersedia")

elif pilihan == 4:
        print("\n--- Konversi Waktu ---")
        print("1. Menit ke Detik")
        print("2. Jam ke Detik")
        sub = int(input("Pilih konversi: "))

        if sub == 1:
            menit = float(input("Masukkan waktu (Menit): "))
            print("Hasil:", menit*60, "detik")
        elif sub == 2:
            jam = float(input("Masukkan waktu (Jam): "))
            print("Hasil:", jam*3600, "detik")
        else:
            print("Pilihan tidak tersedia")

elif pilihan == 5:
        print("\n--- Konversi Mata Uang ---")
        print("1. Dollar ke Rupiah")
        print("2. Rupiah ke Dollar")
        print("3. Rupiah ke Poundsterling")
        print("4. Poundsterling ke Rupiah")
        print("5. Yen ke Rupiah")
        print("6. Rupiah ke Yen")  
        sub = int(input("Pilih konversi: "))

        if sub == 1:
            dollar = float(input("Masukkan mata uang (Dollar): "))
            print("Hasil:", dollar*16669.95, "Rupiah")
        elif sub == 2:
            rupiah = float(input("Masukkan mata uang (Rupiah): "))
            print("Hasil:", rupiah*0.000060, "Dollar")
        elif sub == 3:
            rupiah = float(input("Masukkan mata uang (Rupiah): "))
            print("Hasil:", rupiah*0.000045, "Poundsterling")
        elif sub == 4:
            poundsterling = float(input("Masukkan mata uang (Poundsterling): "))
            print("Hasil:", poundsterling*22414.02, "Rupiah")
        elif sub == 5:
            yen = float(input("Masukkan mata uang (Yen): "))
            print("Hasil:", yen*112.65, "Rupiah")
        elif sub == 6:
            rupiah = float(input("Masukkan mata uang (Rupiah): "))
            print("Hasil:", rupiah*0.0089, "Yen")
        else:
            print("Pilihan tidak tersedia")

            