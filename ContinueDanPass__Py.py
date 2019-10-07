Kres = '#'
Judul1 = "PENGGUNAAN FOR...ELSE - BIASA"
Judul2 = "PENGGUNAAN FOR...ELSE - DENGAN BREAK"
Judul3 = "PENGGUNAAN FOR...ELSE - DENGAN CONTINUE"
Judul4 = "PENGGUNAAN FOR...ELSE - DENGAN PASS"


#----------------------------BAGIAN 1----------------------------
print(Kres * 2, Judul1, Kres * 2)

for X in range(1, 11):
    print("Contoh Nilai Urutan ke : ", X)
else:
    print("Akhir Dari Loop")
print("Print diluar loop\n\n")


#----------------------------BAGIAN 2----------------------------
print(Kres * 2, Judul2, Kres * 2)

for X in range(1, 11):
    print("Contoh Nilai Urutan ke : ", X)

    if X == 6:
        print("Angka :", X, "Ditemukan!\n\n")
        break
else:
    print("Selesai")


#----------------------------BAGIAN 3----------------------------
print(Kres * 2, Judul3, Kres * 2)

for X in range(1, 11):
    print("Contoh Nilai Urutan ke : ", X)

    if X == 7:
        print("Angka :", X, "Ditemukan!")
        continue 
else:
    print("Selesai\n\n")


#----------------------------BAGIAN 4----------------------------
print(Kres * 2, Judul4, Kres * 2)

for X in range(1, 11):

    if X == 4:
        print("Angka :", X, "Ditemukan!")
        pass
        print("Cek!")

    print("Nilai saat ini adalah :", X)
else:
    print("Selesai\n\n")



