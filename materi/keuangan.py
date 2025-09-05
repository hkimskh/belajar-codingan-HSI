import csv
file_path = r"/home/abdulhakim/Dokumen/dev/murajaah-csv/tugaskeuangan.csv"
h}"with open(file_path, "r") as file_keuangan:
    next(file_keuangan)
    read = csv.reader(file_keuangan) 
    list_read =list(read)
    print("semua data")
    print("-" * 25)
    print("Tanggal | keterangan | kategori | jumlah")
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori = baris[2]
        jumlah = baris[3]
        
        print(f"{tanggal} | {keterangan} | {kategori} | {jumlah}")