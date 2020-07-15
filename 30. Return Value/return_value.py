# Belajar Method Return Value
# Ada 2 Jenis Method yaitu
# Method Procedure hanya mengeksekusi kode program saja
# Method Function yang mengembalikan nilai
# Return untuk mengembalikan hasil kode program dari method

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka  
    return (list_angka, total)

list_angka, total = jumlahkan(10, 10, 10, 10, 10, 10, 10)

# Menampilkan nilai total dengan return
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")