# Belajar Membuat Method / Function
# Tempat menyimpan kode blok dimana akan dieksekusi jika dipanggil

nama = []

def print_nama():
    print("==================")
    for data in nama:
        print(data)

nama.append("Mas")
print_nama()

nama.append("Her")
print_nama()

nama.append("Botang")
print_nama()