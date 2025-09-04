#materi -python data structure
#1. list [] berurutan, bisa diubah, boleh duplikat
print(".....list.....")
daftarBelanja = ["teh desa", "pisang kembung", "roti gabin", "pocari"]

#mengakses list lewat indeks
print("\nisi tas belanja:", daftarBelanja)
print("item ke 1:", daftarBelanja[0])
print("item ke 2:", daftarBelanja[1])
print("item ke 3:", daftarBelanja[2])
#mengubah isi list
buah = ["apel", "jeruk", "durian"]
print("\n", buah)
buah[0] = "melon"
print(buah)

#menambahkan elemen
#nambahin indeks di tengah
buah.insert(0, "anggur")
print(buah)
# append() menambah item baru diakhir list
daftarBelanja.append("ayam")
print("\nisi tas belanja sekarang:", daftarBelanja)
print("item ke 4:", daftarBelanja[3])



# remove() menghapus item dari list
daftarBelanja.remove("roti gabin")
print("\nisi tas belanja akhir:", daftarBelanja)
#menghapus berdasarkan indeks
daftarBelanja.pop(1)
print("\n", daftarBelanja)

#mengetahui jumlah list
print(len(daftarBelanja))

#mencetak seluruh isi list menggunakan looping
for item in daftarBelanja:
    print("\n", item) 

#manipulasi list lanjutan
jajanThoriq = ["naspad", "es teh"]
jajanIbrohim = ["nasgor", "es jeruk"]
jajanThoriqDanIbrohim = jajanThoriq + jajanIbrohim
print(jajanThoriqDanIbrohim)


#list multi dimensi
list_minuman = [
["kopi", "susu", "teh"], 
["jus apel", "jus jeruk", "jus jambu"],
["es teler", "es campur", "es kelapa"],
]
print(list_minuman)





print("\n-----tuple-----")
# tuple ()   ("")(berurutan, tak bisa di ubah, boleh duplikat
tempat_tgl_lahir = ("bandung", 1, "juli", 1998)
print("tgl lahir ujang:", tempat_tgl_lahir)

#mengakses data tuple lewat index
print("\ntempat:", tempat_tgl_lahir[0])
print("tanggal:", tempat_tgl_lahir[1])
print("Bulan:", tempat_tgl_lahir[2])
print("Tahun lahir:", tempat_tgl_lahir[3])

#akses beberapa indeks sekaligus
# akses bulan (posisi indeks) : lalu batas akhir item nya
print("bulan, tahun:", tempat_tgl_lahir[2:4])

#unpacking tuple ke variable baru
#mengikuti urutan itemnya
tempat_lahir, tgl_lahir, bulan_lahir, thn_lahir = tempat_tgl_lahir
print(tempat_lahir)

















