from colorama import init,Fore,Back,Style
from hero import hero
from mage import mage
from fighter import fighter
from assasin import assasin
from monster import monster

#Reset warna di terminal
init(autoreset=True)


print("================================")
print( Fore.WHITE + Back.GREEN + f"TIM MEMASUKIN ARENA TEMPUR\n")
yuzhong = hero("yuzhong", 1, 2000, 0, "fighter")
gusion = hero("gusion", 1, 1900, 100, "assasin")
kadita = hero("kadita", 1, 1800, 160, "mage")
print("================================")

print("MONSTER MEMASUKIN ARENA TEMPUR\n")
lord = monster("THE LORD", 999, 999)
print("================================")

party = [
    yuzhong,
    gusion,
    kadita
]
print(f"{len(party)} Pasukan siap bertempur")
print("================================")

# print("PERANG DI MULAI\n")
# print(yuzhong)
#print(f"darah yuzhong {yuzhong.get_hp()}")
#yuzhong.set_hp(1000)
yuzhong.hp = 240
kadita.hp = -40
print(f" HP Yuzhong: {yuzhong.hp}")
print(f" HP Kadita: {kadita.hp}")
#print(gusion)
# print(kadita)
# print("\n")
# print(lord)

running = True
while running:
    print(lord)
    print("*** 1. ⚔️ Attack")
    print("*** 2. 🍏 Heal")
    print("*** 3. 🥊 Aksi")
    
    try:
      aksi = int(input("PILIH AKSI : "))
    except ValueError:
      print("Input Error,Hanya Angka!\n")

    if aksi == 1:
        dmg = 100
        yuzhong.atk(lord)
        gusion.atk(lord)
        kadita.atk(lord)
        lord.damaged(dmg * 4)

        if (lord.nyawa == 0):
            print("LORD TERELIMINASI")
            running = False

    elif aksi == 2:
        yuzhong.lifesteal(50)
        
     
    elif aksi == 3:

        print("END GAME")
        print("HASIL PERTANDINGAN")
        print(yuzhong)
        print(gusion)
        print(kadita)
        print("\n")
        print(lord)

    else:
       print("⚠️ pilihan salah, hanya 1-3!\n")

print("================================")


