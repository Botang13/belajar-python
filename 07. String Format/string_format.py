#String Format mempermudah dalam penulisan String, karena tidak harus
#Menggunakan (+) yang banyak sekali

nama_depan = "Herbowo"
nama_tengah = "-Botang-"
nama_belakang = "Prasetyo"

#Tanpa String Format
sapa = "Halo " + nama_depan + " " + nama_tengah + " " + nama_belakang

print(sapa)

#Dengan String Format (Penandanya huruf "f" di depan "" yang menandakan itu String Format)
sapa = f"Halo {nama_depan} {nama_tengah} {nama_belakang}"

print(sapa) 