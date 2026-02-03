print("Hello world")
# cara membuat fungsi
# struktur: def nama_fungsi(parameternya):
def hello(name):
    print(f"Hello barudak, {name}")
#panggil dibawah.  gak boleh nyatu dengan def
hello("Ibrahim")
hello("Usamah")    
hello("eko")

def nilai(nama, uts, uas):
    rumus = (uts + uas) 
    print(f"nilai akhir {nama}: {rumus}")

nilai("Ibrahim", 80, 90)
nilai("Usamah", 70, 85)
nilai("Eko", 75, 95)


def  tahfidz(nama, alquran, tahajji):
    total = (alquran + tahajji)
    print(f"nilai tahfidz {nama}: {total}")

tahfidz("usamah", 90, 85)
