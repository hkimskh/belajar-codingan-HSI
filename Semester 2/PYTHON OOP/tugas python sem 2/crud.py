data = []
# data sebagai array

def tambah_data():
    # variable = .....
    id = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")


    # append fungsinya adalah untuk menambahkan data ke dalam array
    data.append({
        "id": id,
        "nama": nama,
        "kelas": kelas
    })

    print("Data berhasil ditambahkan!")


def tampilkan_data():
    # len = panjang data
    if len(data) == 0:
        print("Data kosong.")
        return
    
    for item in data:
        print("ID:", item["id"], "Nama:", item["nama"], "Dari kelas:", item["kelas"])

tambah_data()
tampilkan_data()