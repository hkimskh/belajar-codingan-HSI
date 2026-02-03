import json
#tambahkan modul 'csv' dengan 'import'
print("")
print("-----read json-----")
file_path_json = r"/home/abdulhakim/Dokumen/dev/materijson/materijson.json"
with open(file_path_json, "r") as file_materi:
    # json.load() >> membaca isi file json
   data_materi = json.load(file_materi)
   # akses data json dgn 'key' nya
   print(f"judul berkas: {data_materi['title']}")
   print(f"Total: {data_materi['total']}")
   print(f"Status Santri: {data_materi['status_santri']}")
   print(f"Status_Lulus: {data_materi['status_lulus']}")
   print(f"Mapel: {data_materi['pelajaran']}")
   #ekstrak data kist dengan for loop
   for pelajaran in data_materi['pelajaran']:
      print(f"---> {pelajaran}")

print("_" * 50) #gandakan simbol dengan perkalian
print("| No | Nama Surah | Ayat | Tempat Turun |")
print("_" * 50)
for surah in data_materi['surah']:
   print(f"| {surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']}")


    