# enumerate() adalah fungsi di Python untuk mengambil index (nomor urut) dan isi data sekaligus saat looping.

class Buku:
    def __init__(self, judul, kategori, stok):
        self.judul = judul
        self.kategori = kategori
        self.stok = stok

    def tampilkan_info(self):
        return f"Judul: {self.judul} | Kategori: {self.kategori} | Stok: {self.stok}"

    def pinjam(self, jumlah_pinjam, nama_peminjam):
        if jumlah_pinjam <= self.stok:
            self.stok -= jumlah_pinjam
            print(f"\n📚 {nama_peminjam} berhasil meminjam {jumlah_pinjam} buku '{self.judul}'.\n")
            print (f"SISA STOK BUKU '{self.judul}' SEKARANG: {self.stok}\n")
            return True
        

        else:
            print(f"❌ Stok tidak mencukupi! Stok tersedia: {self.stok}")
            print(f"😡 LU PUNYA MATA KAGAK?, JELAS JELAS STOK CUMA {self.stok} KOK LU MAU MINJEM {jumlah_pinjam} BUKU {self.judul}, MONYET! 😡😡😡\n ")
            
            return False

    def batas_waktu(self, hari):
        print(f"⏳ Batas waktu pengembalian buku '{self.judul}' adalah {hari} hari.\n")


    def kembalikan(self, jumlah_kembali):
        self.stok += jumlah_kembali
        print(f"📖 Buku '{self.judul}' berhasil dikembalikan sebanyak {jumlah_kembali}.\n")



def tampilkan_menu():
    print("\n=== MENU PERPUSTAKAAN ===")
    print("1. Lihat daftar buku")
    print("2. Pinjam buku")
    print("3. Kembalikan buku")
    print("4. Keluar")


def main():
    print("\n=== SELAMAT DATANG DI PERPUSTAKAAN KAMI !!! ===")
    print("=== PERPUSTAKAAN RAMAH UNTUK SEGALA UMUR ===\n")

    daftar_buku = [
        Buku("FATHUL ALI", "FIQH", 10),
        Buku("AQIDATUNA", "AQIDAH", 7),
        Buku("NABIYYUNA", "SIRAH", 5),
        Buku("ARABIYYAH BAYNA YADAIK ", "BAHASA ARAB", 8),
       
    ]

    # pusing  sekali  ek  💩💩💩💩
    # mulai dari sini kita pake AI wkwkwk 😅 sudah lupa total sistem CLI ( Command Line Interface )

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print("\n📚 DAFTAR BUKU 📚\n")
            for i, buku in enumerate(daftar_buku, start=1):
                print(f"{i}. {buku.tampilkan_info()}")

        elif pilihan == "2":
            print("\n📚 PINJAM BUKU\n")
            for i, buku in enumerate(daftar_buku, start=1):
                print(f"{i}. {buku.tampilkan_info()}")

            pilih = int(input("\nPilih nomor buku: "))
            nama = input("Masukkan nama peminjam: ")
            jumlah = int(input("Masukkan jumlah pinjam: "))

            berhasil = daftar_buku[pilih - 1].pinjam(jumlah, nama)
            if berhasil:
                daftar_buku[pilih - 1].batas_waktu(7)
                print(f"{i}. {buku.tampilkan_info()}")

        elif pilihan == "3":
            print("\n📖 KEMBALIKAN BUKU\n")
            for i, buku in enumerate(daftar_buku, start=1):
                print(f"{i}. {buku.tampilkan_info()}")

            pilih = int(input("\nPilih nomor buku: "))
            jumlah = int(input("Masukkan jumlah kembali: "))

            daftar_buku[pilih - 1].kembalikan(jumlah)


        elif pilihan == "4":
            print("\n👋 Terima kasih sudah berkunjung nyet!")
            break

        else:
            print("❌ Pilihan tidak valid!")


main()
