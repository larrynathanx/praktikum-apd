#KONVERSI TIPE DATA
# bin() – Mengubah integer ke bilangan biner (string)
# bool() – Mengubah ke boolean
# float() – Mengubah ke float
# frozenset() – Membuat himpunan (set) yang tidak bisa diubah
# int() – Mengubah ke integer
# list() – Mengubah ke list
# set() – Membuat set
# str() – Mengubah ke string
# tuple() – Mengubah ke tuple
# type() – Mengecek atau membuat tipe objek 

# num = int("42") # 42
# name = str(123) # "123"
# data = list("abc") # ['a', 'b', 'c']
# data = dict(a=1, b=2) # {'a': 1, 'b': 2}
# print(type(num)) # <class 'int'>

#OPERASI MATEMATIKA
# abs() – Nilai absolut
# divmod() – Mengembalikan tuple (hasil_bagi, sisa_bagi)
# max() – Nilai maksimum
# min() – Nilai minimum
# pow() – Pangkat (dengan opsi modulus)
# round() – Pembulatan angka
# sum() – Penjumlahan iterable
# abs(-9) # 9
# max([1, 3, 7]) # 7
# min([1, 3, 7]) # 1
# round(3.14159,2) # 3.14
# sum([1, 2, 3]) # 6
# pow(2,3) # 8
# divmod(10,3) # Hasil baginya 3, sisa baginya 1

# #CARA PAKE LIBRARY
# import math
# from math import sqrt
# import math as m

# #BUILT IN LIBRARY
# import math
# print(math.sqrt(16))
# print(math.factorial(4))

import random
print(random.randint(1, 4)) # menghasilkan angka random dari 1 - 4
pilih_acak = ["pisang", "rambutan", "manggis"]
acak = "apcb"
print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
print(random.choice(acak)) # memilih 1 karakter acak pada string

kumpulan_angka = "1234567890"
hasil = ""
for i in range(4):
    hasil += random.choice(kumpulan_angka)# memasukkan satu persatu nilai dari kumpulan_angka ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
print(hasil)

acak_kartu = ["1 wajik", "3 wajik", "5 wajik", "as", "king", "queen", "joker", "9 hati", "3 keriting", "4 sekop"]
random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang berubah
print(acak_kartu)








