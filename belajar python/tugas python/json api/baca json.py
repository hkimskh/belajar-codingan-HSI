import json

file_path_json = r"/home/abdulhakim/Dokumen/python3-intro/tugas/json api/json-api-lokal.json"
# Baca file JSON lokal
with open(file_path_json, "r") as file_materi:
    data_materi=json.load(file_materi)

total_pinjam = 0
belum_kembali = 0

print("Belum kembali:")
for anggota in data_materi["anggota"]:
    for buku in anggota["pinjam"]:
        total_pinjam += 1
        if buku["kembali"] == False:  
            belum_kembali += 1
            print(f"- {anggota['nama']} : {buku['judul']} ({buku['tanggal']})")

print(f"Total dipinjam: {total_pinjam} | Belum kembali: {belum_kembali}")