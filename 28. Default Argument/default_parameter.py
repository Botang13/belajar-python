# Belajar Default Argument Value
# Digunakan ketika memanggil method tapi tidak memasukkan parameternya
# Jika lebih dari dua parameter, dua-duanya harus di isi default parameternya
# Atau defaultnya bisa di paramater paling belakang saja

def say_hello(first_name="Default", last_name=""):
    print(f"Hello {first_name} - {last_name}")

say_hello("Her")

# Ingin di inputkan untuk parameter last_name / kedua
say_hello(last_name="Bawaan")

# Posisinya juga bisa di acak, asal menyebutkan parameternya
say_hello(last_name="Bawaan", first_name="Pertama")