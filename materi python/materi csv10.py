import csv
print("materi 10 - file handling")
print("---------------------------")
#BUKA FILE
file_path = r"/home/abdulhakim/Dokumen/dev/sinau/materi-kelas/pesan.txt"
file_pesan = open(file_path, "r")
#baca isi file
isi_pesan = file_pesan.read()
#tampilkan output isi pesan
print(f"ISI PESAN >>> {isi_pesan}")
#tutup file
file_pesan.close()

print("\n-----------------------------------")
print("----read csv file----")
file_path_csv = r"/home/abdulhakim/Dokumen/dev/sinau/materi-kelas/jajan.csv"
file_pesan = open(file_path_csv, "r")
isi_jajan = file_pesan.read()
print(f"UANG JAJAN >>> {isi_jajan}")
file_pesan.close

print("-----APPEND CSV FILE-----")
jajan_baru = [6,"syahid",100000]
print(f"Jajan Baru: {jajan_baru}")
#open() >> membuka file dari file path
#mode 'a' >> (append tambah data)
#new line >> tambah baris baru dengan text kosong
# with......as >> buka file dn tutup otomatis
with open(file_path_csv, "a", newline="") as isi_jajan:
    #aktifkan mode writer csv dr file target
    writer = csv.writer(isi_jajan)
    # tambahkan baris dr variable jajan baru
    writer.writerow(jajan_baru)


