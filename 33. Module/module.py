# Belajar Module
# Karena tidak mungkin membuat program dalam 1 file
# Maka Module dapat memecahnya jadi beberapa file

# Mengambil semua method di file function
import function

hello = function.say_hello("Mas")
print(hello)

hasil = function.total(1,2,3,4,5)
print(hasil)

# Untuk mengambil 1 atau 2 method saja
# Jika ada banyak method dalam satu file
from function import say_hello
from function import total

# Tidak perlu menambahkan prefix nama modulenya
hello = say_hello("Mas")
print(hello)

hasil = total(10,20,30,40,50)
print(hasil)
