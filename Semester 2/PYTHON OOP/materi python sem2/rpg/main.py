from hero import hero #panggil class hero
from mage import mage #panggil class mage
from warior import warrior #panggil class warrior
from assasin import assasin #panggil class assasin
from archer import archer #panggil class archer
from monster import monster #panggil class monster
# summon semua hero
print("== SUMMON HERO ==")
alucard = warrior("ALUCARD", 10, 100, 100, "warrior")
alok = mage("ALOK", 1, 100, 100, "mage ")
hayabusa = assasin("HAYABUSA", 1, 100, 100, "assasin")
layla = archer("LAYLA", 1, 100, 100, "archer")

print("\n== SUMMON MONSTER ==\n")
salamander = monster("SALAMANDER", 100, 1000, 1000)



# alok.attack(alucard)
# alucard.damaged(10)
# alok.critical(alucard)
# print(alucard)
# print(alok)
print("== MULAI GUILD PARTY ==")

print("\n-- Battle Start --\n")
guild_party = [
    alucard,
    alok,
    hayabusa, 
    layla
]

print("\nKomandan: 'PASUKAN SIAP!'")
print(F"Total {len(guild_party)} pahlawan")

print("\nKomandan: 'RAID DI MULAI!'\n")
alucard.critical(salamander)
alok.critical(salamander)
alok.cast_spell(salamander)

# pasang cheat hp + 1000
# print(f"HP alucard: {alucard.get_hp()}")
# alucard.set_hp(100)

# print(alucard)
# print(alok)
# print(hayabusa)
# print(layla)
# print(salamander)

running = True
while running:
    print(salamander)
    print("1. Attack, 2. Heal, 3. Exit")

    aksi = int(input(">> pilih aksi:"))
    if aksi == 1:
        dmg = 10
        for party in guild_party:
            party.attack(salamander)
            salamander.damaged(dmg)

        if (salamander.hp == 0):
            print("yey! monster telah dikalahkan")
            running = False
    elif aksi == 2:
        alok.heal(10) 

    elif aksi == 3:
        print("game berakhir...")
        running = False       

    



