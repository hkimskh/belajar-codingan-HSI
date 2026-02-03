# senin, 26 januari 2026
from hero import hero #panggil class hero

class assasin(hero):
    def __init__(self, name, level, hp, mana, role):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        super().__init__(name, level, hp, mana, role="assasin")
        print(f"hero [{self.role}] {self.name} telah di summon!")


    def critical(self, target):
        dmg = 50
        print(f"{self.name} menggunakan: SHADOW KILL")
        print(f"👹 {target.name} terkena critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
