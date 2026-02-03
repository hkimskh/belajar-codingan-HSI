print("---materi 8 - functional---")
print("================================")
#function di awal dengan keyword "def"
#fungsi/def baru bisa dipanggil setelah di buat
def halo_bre():
    print("halo bre")
    print("sehat kan bre?")
halo_bre()

#function dengan parameter nama
def sapaan(nama):
    print("gimana kabarnya", nama)
    print("sehatkan?")
    print("------------------------------")
    
print("\n cobain fungsinya")
sapaan("ibrahim")    
sapaan("bilal")
sapaan("dalilah")
sapaan("aini")
sapaan("usamah")

#praktek luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    print("--> panjang=", panjang)
    print("--> lebar=", lebar)
    rumus = panjang * lebar
    print("luas_persegi_panjang=", rumus)

luas_persegi_panjang(15, 10)



#contoh lagii
def say_hello(name):
    print(f"halo {name}")
    print("baek baek ae")
say_hello("azzam")
say_hello("syahid")



