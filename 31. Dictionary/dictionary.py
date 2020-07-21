# Belajar Tipe Data Dictionary
# Dapat mengganti index dengan string
# Index disebut key
# Biasa digunakan untuk membuat kumpulan data seperti customer ini
# Karena kemudahan mengakses datanya (Tidak Perlu Index)

customer = {"Name":"Mas", "Age":23, "Address":"Jogja"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "Mas Botang"

del customer["Address"]

# Menggunakan Perulangan Biasa
for key in customer:
    value = customer[key]
    print(f"{key}:{value}")

# Menggunakan Items
for key, value in customer.items():
    print(f"{key}:{value}")

# Print Items
print(customer.items())