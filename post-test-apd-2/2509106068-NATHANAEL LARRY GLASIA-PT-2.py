suhu = ["27", "33", "46", "55", "67","92"]
suhu_1 = 27
suhu_2 = 33
suhu_3 = 46
suhu_4 = 55
suhu_5 = 67
suhu_6 = 92

#Rumus 

#fahrenheit = (9/5*c) + 32
#kelvin = c + 273.15
#reamur = (4/5)*c

suhu1f = (9/5*27) + 32
suhu2f = (9/5*33) + 32
suhu3k = 46 + 273.15
suhu4k = 55 + 273.15
suhu5r = (4/5)* 67
suhu6r = (4/5)* 92

jumlah = suhu1f + suhu2f + suhu3k + suhu4k + suhu5r + suhu6r

rata2 = jumlah/len(suhu)

NIM = 68

Bolean = NIM < rata2

print("Suhu_1 =", suhu_1)
print("Suhu_2 =", suhu_2)
print("Suhu_3 =", suhu_3)
print("Suhu_4 =", suhu_4)
print("Suhu_5 =", suhu_5)
print("Suhu_6 =", suhu_6)

print("fahreinheit suhu_1 =", suhu1f)
print("fahrenheit suhu_2 =", suhu2f)
print("kelvin suhu_3 =", suhu3k)
print("kelvin suhu_4 =", suhu4k)
print("reamur suhu_5 =", suhu5r)
print("reamur suhu_6 =", suhu6r)

print("jumlah =", jumlah)
print("rata2 =", rata2)
print("NIM =", NIM)
print("Bolean =", Bolean)

print("suhu =", suhu[-4:])