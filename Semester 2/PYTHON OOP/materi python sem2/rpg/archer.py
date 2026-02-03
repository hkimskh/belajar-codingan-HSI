# senin, 26 januari 2026
from hero import hero #panggil class hero

class archer(hero):
    def __init__(self, name, level, hp, mana, role):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        super().__init__(name, level, hp, mana, role="archer")
        print(f"hero [{self.role}] {self.name} telah di summon!")


    def critical(self, target):
        dmg = 50
        print(f"👹 {self.name} terkena critical {dmg} DMG!")
        self.attack(target)
        target.damaged(dmg)
