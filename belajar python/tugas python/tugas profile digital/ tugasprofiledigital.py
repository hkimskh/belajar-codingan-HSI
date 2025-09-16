

#TUGAS BIKIN PROFIL DIGITAL
print("====≽Tentang Kamu≼====")
nama = input("namamu?: ")
umur = input("berapa umurmu?: ")
kelas = input ("kamu kelas berapa?: ")
hobi = input ("apa hobimu?: ")
citaCita = input("apa cita cita mu?: ")
waktuBelajar = input("waktu belajar ternyaman?: ")
tahunLahir = int(input("tahun lahirmu?: ")) 


print("\n>>>>>tipe digital<<<<<")

print("1. wibu")
print("2.Kpopers")
print("3.anak nongki")
print("4.gamer")
tipe = input("kamu termasuk yang mana?: ")
if tipe == "wibu":
    print("kamu pasti sering nonton anime sambil berak 😂")
    waifu = input("siapa waifumu?: ")
    print(waifu, "sangat cantik")
elif tipe == "gamer":
    game = input("apa game kesukaanmu?: ")
    print("pasti kamu sangat ahli dalam bermain", game)
elif tipe == "kpopers":
    bias = input("siapa bias kamu?: ")
    print(bias, "\t?" "selera yang bagus!")
elif tipe == "anak nongki":
    print("kamu pasti anak beban di tongkrongan😂")
    tempat_tongkrongan = input("dimana kamu biasa nongkrong?: " )  
    print(tempat_tongkrongan, "\t🤔?" "selera yang lumayan")     

print("\n<====fun check====>")
bau = input("temen sebelah bau ya/gak: ")
if bau == "ya":
    print("waduh, cepet suruh makan stella tuh")
elif bau == "gak":
    print("oh, iyalah gak kayak lu!, bau!")



# hasil
print("\n▌│█║▌║▌║Tentang Kamu▌│█║▌║▌║")
print("\nNama: ", nama)
print("Umur: ", umur)
print("Kelas: ", kelas)
print("Hobi: ", hobi)
print("Cita cita: ", citaCita)
print("Waktu belajar ternyaman:", waktuBelajar)
print("Tahun Lahir: ", tahunLahir)

print("\n<<<<<=Tipe Digital=>>>>>")
print("kamu adalah" "\t", tipe)
if tipe == "wibu":
    print("waifu mu adalah" "\t", waifu)
elif tipe == "gamer":
    print("game kesukaanmu adalah" "\t", game)
elif tipe == "kpopers":
    print("bias kamu adalah" "\t", bias)  
elif tipe == "anak nongki":
    print("tempat tongkrongan kesukaanmu adalah" "\t", tempat_tongkrongan ) 

print("\n.....fun check.....")
print("temen sebelah kamu bau apa gak?")
if bau == "ya":
    print("waduh, cepet suruh makan stella tuh")
elif bau == "gak":
    print("oh, iyalah gak kayak lu!, bau!")          





            





                









