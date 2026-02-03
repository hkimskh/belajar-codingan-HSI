import csv
#tambahkan modul 'csv' dengan 'import'
print("materi 11 - file handling part 2")
print("-----UPDATE CSV-----")
#baca semua file >>> ekstrak data >>> buat data baru
# ---> tulis ulang semua isi barisnya dgn mode 'w'
file_path_csv = r"/home/abdulhakim/Dokumen/dev/sinau/materi-kelas/jajan.csv"
# siapkan data jajan kosong 
# utk menampung data dari csv kelist
data_jajan = []
with open(file_path_csv, "r") as isi_jajan:
    # csv.reader() >>> membaca isi file csv
    isi_tabel_jajan = csv.reader(isi_jajan)
    #ekstrak semua data dengan for loop
    for item_jajan in isi_tabel_jajan:
        print(item_jajan)
        #tambah item ke list data jajan
        data_jajan.append(item_jajan)

# 2. memgubah atau membuat data baru
for item in data_jajan:
    print(f"Item ke-{item[0]} = {item}")
    #jika kolom nama adalah "x nama"
    if item[1] == "Hanif":
        #ganti kolom uang jajan dgn nilai baru
        uang_jajan_baru = 15000
        item[2] = uang_jajan_baru
        print(f"data yang akan diganti di temukan ganti uang jajan {uang_jajan_baru}")
    print("------loop end----")        

#ganti kolom uang (index 2) dengan nilai baru
print(f"data jajanan terkini: {data_jajan}")



# 3.hapus data di list by index
del data_jajan[2]
print(f"data jajanan terkini: {data_jajan}")


# tulis ulang data dengn mode 'w' => write

with open(file_path_csv, "w", newline="") as isi_jajan:
    writer = csv.writer(isi_jajan)

    # .writerows() >> tulis sekali banyak
    writer.writerows(data_jajan)
