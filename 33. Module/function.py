# Belajar Module
# Karena tidak mungkin membuat program dalam 1 file
# Maka Module dapat memecahnya jadi beberapa file

def say_hello(nama):
    return f"Hello {nama}"

def total(*list_angka):
    hasil = 0
    for data in list_angka:
        hasil = hasil + data
    return hasil