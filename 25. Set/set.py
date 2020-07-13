#Belajar Set

#List => []
#Tuple => ()
#Set => {}

#List dapat memasukkan data yang sama begitu juga tuple
#Set harus Unique hanya menampilkan 1 data yang sama saja meskipun ada banyak
#Tidak dijamin ordernya / indeksnya karena berubah tiap waktu, 
#karenanya tidak dapat diakses menggunakan indeks

nama = {"Mas", "Her", "Mas", "Her", "Botang"}

print(nama)

#Menambag data di set
nama.add("P")
nama.add("P")

#Menggunakan For Loop
for i in nama:
    print(i)

nama.remove("Mas")

print(nama)