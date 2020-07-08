#Belajar Elif => Else If

#Jika memilih 1 dan 2 maka Menu tidak tersedia akan ditampilkan
#Hal ini karena jika memilih 1 dan 2, program akan mengeksekusi semuanya
#Dan else akan ikut ditampilkan karena tiap if dianggap blok yang berbeda
#Namun jika memilih 3, tidak akan dieksekusi karena bernilai benar

menu_pilihan = input("Silahkan Pilih Menu [1-3] : ")

if menu_pilihan == "1":
    print("Anda Memilih Menu 1")

if menu_pilihan == "2":
    print("Anda Memilih Menu 2")

if menu_pilihan == "3":
    print("Anda Memilih Menu 3")

else:
    print("Menu Tidak Tersedia")

if menu_pilihan == "x":
    print("Program Tidak Keluar")

#Menggabungkan if dalam satu blok dengan elif
#Jadi tidak akan mengeksekusi if lainnya jika sudah kondisi True

menu_pilihan = input("Silahkan Pilih Menu [1-3] : ")

if menu_pilihan == "1":
    print("Anda Memilih Menu 1")

elif menu_pilihan == "2":
    print("Anda Memilih Menu 2")

elif menu_pilihan == "3":
    print("Anda Memilih Menu 3")

else:
    print("Menu Tidak Tersedia")
