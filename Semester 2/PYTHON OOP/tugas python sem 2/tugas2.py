class Hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        ...
        # hero / normal / boss
        
        self.name = name
        self.job = job
        self.hp = hp
        self.type = hero_type
        self.max_hp = hp
        print(f"✨ {self.name} [{self.job}] memasuki arena!")


        # - cek hero masih hidup
    def __str__(self):
        status = "HIDUP"
        if self.hp == 0:
            status = "MATI"
        return f"{self.name} [{self.type}] | {self.job} | HP: {self.hp} STATUS : {status} "

    def is_alive(self):
        return self.hp > 0
        

    
    
        
        
        
    def attack(self, enemy, damage):
        
        # - cek hero masih hidup
        
        # - cek damage valid
        print(f"⚔️ {self.name} menyerang {enemy.name}, damage = {damage} ")

        # - boss rage mode jika HP <= 50%

        
        if self.type == "BOSS" and self.hp <= self.max_hp / 2:
            damage*2
            
            print(f"😈 {self.name} DALAM RAGE MODE !!!")
        
    def take_damage(self, damage):
        # TODO:
        # - kurangi HP
        self.hp -= damage
        print(f"💥 {self.name} menerima damage sebesar {damage} dmg")
       
        # - HP tidak boleh < 0
        if self.hp < 0: 
            self.hp = 0 
        # - tampilkan pesan jika mati
            print(f"SISA HP {self.name}: {self.hp} ")
            print(f"💀 {self.name} telah tereliminasi!")
            print(f"{self.name} tidak bisa melanjutkan pertempuran")

        if self.type == "BOSS" and self.hp == 0:

            print(f"💀 {self.name} SI BABI HAMA TELAH MATI !!!")    

                  
        

    def heal(self, ngeheal):
        # TODO:
        # - hero mati tidak bisa heal
        if self.hp == 0:
            print(f"💀 {self.name} sudah tereliminasi, {self.name} tidak bisa ngeheal !!!")
            
        # - heal sesuai role
        if self.job == "HEALAER":
            self.hp += ngeheal * 2
            print(f"❤️ {self.name} melakukan heal sebesar {ngeheal*2} HP")

        else: 
            self.hp += ngeheal
            print(f"❤️ {self.name} melakukan heal sebesar {ngeheal} HP")    

        pass

dyroth = Hero("DYROTH", "FIHTER", 100, "HERO")
angela = Hero("ANGELA", "MAGE", 80, "HERO")
estes = Hero("ESTES", "HEALAER", 80, "HERO")
hayabusa = Hero("HAYABUSA", "ASSASSIN", 120, "HERO")


print("\n--- PARTY MEMASUKI DUNGEON ---\n")
print("💫 DYROTH MASUK DUNGEON")
print("💫 ANGELA MASUK DUNGEON")
print("💫 ESTES MASUK DUNGEON")

print("\n--- 🐺 WOLF MUNCUL !!! ---\n")
wolf = Hero("WOLF", "MONSTER", 200, "NORMAL")

print("\n--- BATTLE START !!! ---\n")
dyroth.attack(wolf, 30)
wolf.take_damage(30)
print(f"SISA HP WOLF: {wolf.hp}\n")
dyroth.attack(wolf, 50)
wolf.take_damage(50)
print(f"SISA HP WOLF: {wolf.hp}\n")
wolf.attack(dyroth, 50)
dyroth.take_damage(50)
dyroth.heal(45)
print(f"SISA HP DYROTH: {dyroth.hp}\n")
dyroth.attack(wolf, 200)
wolf.take_damage(200)
print(f"SISA HP WOLF: {wolf.hp}\n")
print(wolf)

# babi hama (minotaurus) muncul

print("\n--- 🐗 MINOTAURUS MUNCUL !!! ---\n")
minotaurus = Hero("MINOTAURUS", "PENJAGA DUNGEON", 600, "BOSS")

print("\n--- BATTLE START !!! ---\n")
hayabusa.attack(minotaurus, 95)
minotaurus.take_damage(95)
minotaurus.heal(30)
print(f"SISA HP MINOTAURUS: {minotaurus.hp}\n")
angela.attack(minotaurus, 20)
minotaurus.take_damage(20)
print(f"SISA HP MINOTAURUS: {minotaurus.hp}\n")
dyroth.attack(minotaurus, 45)
minotaurus.take_damage(45)
print(f"SISA HP MINOTAURUS: {minotaurus.hp}\n")
minotaurus.attack(hayabusa, 80)
hayabusa.take_damage(80)
print(f"SISA HP HAYABUSA: {hayabusa.hp}\n")
hayabusa.heal(40)
print(f"SISA HP HAYABUSA: {hayabusa.hp}\n")
dyroth.attack(minotaurus, 300)
minotaurus.take_damage(300)
minotaurus.heal(100)
minotaurus.attack(dyroth, 50)
dyroth.take_damage(50)
minotaurus.attack(angela, 70)
angela.take_damage(70)

print(f"SISA HP MINOTAURUS: {minotaurus.hp}\n")
estes.attack(minotaurus, 40)
minotaurus.take_damage(40)
print(f"SISA HP MINOTAURUS: {minotaurus.hp}\n")
hayabusa.attack(minotaurus, 300)
minotaurus.take_damage(300)

# MATI KAN LU BABI HAMA
print(f"\nPERTEMPURAN SELESAI !!!")






