

class Adadachi:
    def __init__(self,name, personality):
        self.name = name
        self.hunger = 2
        self.happiness = 1
        self.personality = personality
        self.poop_lvl = 0
    
    
    def favorite_food(self):
        return self.personality["fav_food"]
    
    def hates_food(self):
        return self.personality["hates_food"]

    def favorite_game(self):
        return self.personality["fav_game"]
    
    def hates_game(self):
        return self.personality["hates_game"]

    def change_poop_levels(self):
        if self.hunger <= 3:
            self.poop_lvl += 1
            self.happiness -= 1
