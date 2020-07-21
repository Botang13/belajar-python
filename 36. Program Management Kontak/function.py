# Program Management Kontak

# Method Lihat Daftar Kontak
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("========================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"No. Telepon : {kontak['telepon']}")

# Method tambah kontak
def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("No. Telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

# Method hapus kontak
def hapus_kontak(daftar_kontak):
    telepon = input("No. Telepon yang ingin dihapus : ")
    
    # Mencegah No. Telepon tidak ketemu karena index dimulai dari 0
    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break

    if index == -1:
        print("Data tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Berhasil menghapus data kontak")

# Method cari kontak
def cari_kontak(daftar_kontak):
    nama_yang_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"] 
        # Jika tidak negatif 1, maka data ketemu
        # Lower digunakan karena data dummynya huruf kecil
        # Karena python case sensitive
        if nama.lower().find(nama_yang_dicari.lower()) != -1:
            print("========================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"No. Telepon : {kontak['telepon']}")