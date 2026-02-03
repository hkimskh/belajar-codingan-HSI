class monster: 
    #self = dirinya sendiri / internal
    def __init__(self, name, level, hp, mana,):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        
        print(f"hero {self.name} telah di summon!")

    def __str__(self):
        status = "hidup"
        if self.hp == 0:
            status = "mati"

        return f"[MONSTER] {self.name} | HP: {self.hp} STATUS : {status} " 


    def damaged(self, damage):
        self.hp -= damage
        print(f"💥 hero {self.name} terkena {damage} damage!")
        if self.hp == 0:
            print(f"{self.name} telah tereliminasi!")
       
    