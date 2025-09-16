#lambda untuk menulis fungsi yang ringkas dgn 1 baris saja
#sering disebut juga fungsi anonim (tanpa nama)
sapa = lambda name: print(f"halo {name}")
sapa("hakim")
sapa("bilal")

#contoh penerapan lambda dengan higher-order function
#map() -- sorted() -- filter()
print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
jajan_mingguan = [50000, 30000, 45000, 70000]
#sorted >>>> untuk mengurutkan data
urutkan_uang = sorted(jajan_mingguan)
print(f"\nurutan uang: {urutkan_uang}")
UrutkanUangTerbalik = sorted(jajan_mingguan, reverse=True)
print(f"urutkan uang terbalik: {UrutkanUangTerbalik}")
 
#map >>>>> mentransformasi data
kuranginUang = map(lambda uang: uang - 5000, jajan_mingguan)
#list mengubah data objek map menjadi bentuk list
listKuranginUang = list(kuranginUang)
print(f"\nmap uang berkurang: {listKuranginUang}")

#filter >>>> menyaring / memfilter data
jajanBanyak = filter(lambda uang: uang >= 30000, jajan_mingguan)
list_jajan_banyak = list[jajanBanyak]
print(f"filter jajan diatas 30ribu: {list_jajan_banyak}")