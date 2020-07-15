# Belajar Argument List
# Membuat 1 argumen / parameter dapat dimasukkan banyak nilai
# Hanya bisa 1 argumen list saja dalam method
# Untuk dua parameter, list bisa ditaruh paling belakang

def jumlahkan(x, *list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka  
    print(f"Total {list_angka} = {total}")

# Nilai pertama masuk ke parameter x, sisanya ke list
# Makanya hasil menjadi 60 (dari total 70) karena tidak ditambahkan di total
jumlahkan(10, 10, 10, 10, 10, 10, 10)