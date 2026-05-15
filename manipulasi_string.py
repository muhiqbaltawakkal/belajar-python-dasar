nama = "Budi"
umur = 25

pesan = "Nama saya " + nama + ", umur " + str(umur)
print(pesan)

print(len(nama))
print(len(pesan))

nama = "Python"
print(nama[0])
print(nama[1])
print(nama[2])

print(nama[-1])
print(nama[-2])
print(nama[-3])

nama = "Python"
print(nama[:])
print(nama[0:3])
print(nama[2:])

nama = "Alice"
print(nama)
nama_upper = nama.upper()
print(nama_upper)
nama_lower = nama.lower()
print(nama_lower)

nama = "eko kurniawan"
nama_title = nama.title()
print(nama_title)
nama_capilized = nama.capitalize()
print(nama_capilized)

nama = "   Eko    "
name_strip = nama.strip()
print(name_strip)

kalimat = "I love Java"
kalimat_baru = kalimat.replace("Java", "Python")
print(kalimat_baru)

nama = "eko kurniawan khannedy"
jumlah_k = nama.count("eko")
print(jumlah_k)

kalimat = "Python Programming"
posisi = kalimat.find("Programming")
print(posisi)

kalimat = "Baris pertama\nBaris kedua"
print(kalimat)

kalimat = "Nama:\tEko\nUmur:\t30"
print(kalimat)

lokasi = "C:\\\\Users\\\\Eko\\\\Desktop"
print(lokasi)

kalimat = "Dia berkata \"Hello\" kepada saya"
print(kalimat)

nama = "Eko"
umur = 30
kota = "Jakarta"

kalimat = f"Halo, nama saya {nama}, umur saya {umur}, tinggal di {kota}"
print(kalimat)

harga = 10000
jumlah = 3

total = f"Total : {harga * jumlah}"
print(total)

nama = "eko kurniawan"
kalimat = f"Hello {nama.upper()}"
print(kalimat)