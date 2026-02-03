import csv

file_path = r"/home/abdulhakim/Dokumen/dev/murajaah-csv/data.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read =list(read)
    #pake list biar g muncul objek objek objek objek 
    print("semua data")
    print("-" * 25)
    for baris in list_read:
        nomor = baris[0]
        nama = baris[1]
        kelas = baris[2]

        print(f"| {nomor} | {nama} | {kelas} |")


    with open(file_path, 'a', newline="") as file_baru:
         write = csv.writer(file_baru)
         write.writerow({"5","Bilal","10"})
    
