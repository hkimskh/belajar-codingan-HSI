 #selasa, 20 januari 2026
#definisikan class NamaClass
class cat:
    
    # __init__  = constructor = yg pertama kali di akses/dipanggil
    # definisikan atributnya di dalam constructor
    def __init__(self, color, height):
        self.color = color
        self.height = height
    

#buat objek dari class cat
garfield = cat("orange", 25)
persia = cat("white", 20)
#debug objek di memory kita, muncul address 0x...
print("Obj Garfield:", garfield)
print("Obj Persia:", persia)
# panggil nama atribut dr objek
print(f"Warna garfield: {garfield.color}")
print(f"Tinggi garfield: {garfield.height}")



#COBA-COBA SENDIRI TOT
class santri:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

#buat objek dari class santri 
bilal = santri("bilal", 16)   
ibrahim = santri("ibrahim", 18)   
#debug objek di memory kita, muncul address 0x...
print("Obj Bilal:", bilal)
print("Obj Ibrahim:", ibrahim)
# panggil nama atribut dr objek
print(f"data bilal: nama: {bilal.nama}, umur: {bilal.umur}")


#----------------------------------------------------------


# # Kamis, 22 januari 2026


# class hero: 
#     #self = dirinya sendiri / internal
#     def __init__(self, name, level, hp, mana):
#         self.name = name
#         self.level = level
#         self.hp = hp
#         self.mana = mana
#         print(f"hero {self.name} telah di summon!")
#         # mengganti print objek dari bentuk memori 0x...
#         #  ke bentuk string yg lebih informatif/enak dibaca
#     def __str__(self):
#         status = "hidup"
#         if self.hp == 0:
#             status = "mati"

#         return f"[{self.name}] | HP: {self.hp} STATUS : {status} "        

#     def damaged(self, damage):
#         self.hp -= damage
#         print(f"hero {self.name} terkena {damage} damage!")
#         if self.hp == 0:
#             print(f"{self.name} telah tereliminasi!")


#     def attack(self, enemy):
#         print(f"⚔️  hero {self.name} menyerang {enemy.name}!")  


#     def heal(self, amount):
#         self.hp += amount
#         print(f"❤️  hero {self.name} mendapatkan heal sebesar +{amount} HP!")       


# #panggil/summon heronya (buat objeknya )
# alucard = hero("ALUCARD", 10, 100, 100)
# eudora = hero("EUDORA", 10, 100, 100)
# # print(alucard, eudora)
# print("BATTLE START!")
# alucard.attack(eudora)
# eudora.damaged(10)
# #di balas bwaang
# eudora.attack (alucard)
# alucard.damaged(5)
# alucard.damaged(5)
# alucard.damaged(5)
# #alucard membalas ulang
# alucard.attack (eudora)
# eudora.damaged(80) 
# print(eudora)
# eudora.heal (50) #eudora di heal
# #eudora menyerang lagi
# eudora.attack (alucard)
# alucard.damaged(80)
# print(alucard)
# alucard.heal(10)

# #cek status terkini
# print(alucard)
# print(eudora)