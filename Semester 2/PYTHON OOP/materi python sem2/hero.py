# Kamis, 22 januari 2026


class hero: 
    #self = dirinya sendiri / internal
    def __init__(self, name, level, hp, mana, role):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.role = role
        print(f"hero [{self.role}] {self.name} telah di summon!")
        # mengganti print objek dari bentuk memori 0x...
        #  ke bentuk string yg lebih informatif/enak dibaca
    def __str__(self):
        status = "hidup"
        if self.hp == 0:
            status = "mati"

        return f"[{self.name}] | HP: {self.hp} STATUS : {status} "        

    def damaged(self, damage):
        self.hp -= damage
        print(f"hero {self.name} terkena {damage} damage!")
        if self.hp == 0:
            print(f"{self.name} telah tereliminasi!")


    def attack(self, enemy):
        print(f"⚔️  hero {self.name} menyerang {enemy.name}!")  


    def heal(self, amount):
        self.hp += amount
        print(f"❤️  hero {self.name} mendapatkan heal sebesar +{amount} HP!")  

    def critical(self, target):
        print(f"👹 {self.name} terkena 0 DMG!!")



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