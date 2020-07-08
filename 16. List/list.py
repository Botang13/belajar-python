#Belajar List
#Tipe data untuk kumpulan data
#List dapat diakses menggunakan index
#Index dimulai dari 0

#Cara 1 Menambah menggunakan Append
nama = []
nama.append("Mas")
nama.append("Her")
nama.append("Botang")

#Cara 2
nama2 = ["Mas", "Her", "Botang"]
nama2.append("Young")
nama2.append("Master")

print(nama)
print(nama2[0])
print(nama2[1])
print(nama2[2])
print(nama2[3])
print(nama2[3],nama[0])
print(nama2)

#Mengetahui panjang List
print(len(nama))
print(len(nama2))

#Menghapus menggunakan Remove
#Saat menghapus data, index akan bergeser. Hati - hati.
nama2.remove("Botang")
print(nama2)
print(len(nama2))
print(nama2[0])
print(nama2[1])
print(nama2[2])
print(nama2[3])