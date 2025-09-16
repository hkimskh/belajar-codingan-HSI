#dictionary (dict) --> {key:value}--> / {kunci:isi}
#berurutan, berubah, tidak duplikat
kamus_anime ={
    "one piece": "monkey D luffy",
    "demon slayer": "Kamado tanjirou",
    "waifu": {
    "one piece": "big mom",
    "demon slayer": "nezuko"
    }
}

#cara mengakses nilai dict
print("kamusanime:", kamus_anime)
print("mc demon slayer:", kamus_anime["demon slayer"])
print("waifu demon slayer:", kamus_anime["waifu"]["demon slayer"])



#nambah item baru di dictionary
kamus_anime["naruto"] = "shikamaru"
print("mc naruto:", kamus_anime["naruto"])

#mengubah item dr dictionary
kamus_anime["demon slayer"] = "zenitsu"
print("kamusanime:", kamus_anime)

#menghapus item dari dictionary
del(kamus_anime["one piece"])
print("kamus anime terbaru:", kamus_anime)
del(kamus_anime["waifu"]["one piece"])
print("kamus anime revisi:", kamus_anime)


#mengecek key (true or false) akan true jika key nya ada
harun = {
    "umur": 15,
    "asal": "bogor"
}
print("umur" in harun)

#cara ngecek semua key aja
print(harun.keys())

#cara ngecek value aja
print(harun.values())

#looping
for key in harun:
    print(key)


for value in harun.values():
    print(value)

for key, value in harun.items():
    print(f"{key} --> {value}")

#cara bikin dict di dalam dict
kelas = { 
    "siswa1": {
    "nama": "harun",
    "umur": 15,
    "asal": "bogor",
    "hobi": {
        "hobi1": "main bola",
        "hobi2": "makan",
    }
    },
    "siswa2": {
        "nama": "juned",
        "umur": 16,
        "asal": "bekasi",
        "hobi": {
            "hobi1": "lompat",
            "hobi2": "main bal"
        }
    }

} 

print(kelas["siswa2"]["nama"])   






