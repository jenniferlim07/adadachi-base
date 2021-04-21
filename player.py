from constants import STATUS
import random
from adadachi import Adadachi

class Player:
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }

    def get_status(self):
        print(f"Name: {self.adadachi.name}")
        print(f"Hunger Level:  {self.adadachi.hunger}")
        print(f"Happiness Level:  {self.adadachi.happiness}")
        print(f"Poop Level:  {self.adadachi.poop_lvl}")


    def feed(self):
        for food in self.inventory["foods"]:
            print(food)

        print(f"\n{self.adadachi.name}'s favorite food is {self.inventory['foods'][self.adadachi.favorite_food()]}")
        print(f"{self.adadachi.name} hates {self.inventory['foods'][self.adadachi.hates_food()]}\n")
        player_picks = input(f"What do you want to feed {self.adadachi.name}? \t").lower()
        
        if player_picks in self.inventory["foods"]:
            self.adadachi.hunger -= 1
            if player_picks == self.inventory['foods'][self.adadachi.favorite_food()]:
                self.adadachi.happiness += 1
                print(f"{self.adadachi.name} loves eating {player_picks}!")

            if player_picks == self.inventory['foods'][self.adadachi.hates_food()]:
                self.adadachi.happiness -= 1
                print(f"{self.adadachi.name} hates eating {player_picks}!")
            print(f"{self.adadachi.name} ate the {player_picks}")
            self.adadachi.change_poop_levels()
        else:
            print("Try again")

    def clean(self):
        self.adadachi.poop_lvl -= 1
        self.adadachi.happiness += 1
        print(f"You cleaned {self.adadachi.name}!")
        print(f"Poop level is now: {self.adadachi.poop_lvl}")
        

    def play_with_adadachi(self):
        for game in self.inventory["games"]:
            print(game)

        print(f"\n{self.adadachi.name}'s favorites game is {self.inventory['games'][self.adadachi.favorite_game()]}")
        print(f"{self.adadachi.name} hates playing {self.inventory['games'][self.adadachi.hates_game()]}\n")

        player_picks = input(f"What do you want to play with {self.adadachi.name}? ").lower()

        if player_picks in self.inventory["games"]:
            self.adadachi.hunger += 1
            if player_picks == self.inventory['games'][self.adadachi.favorite_game()]:
                self.adadachi.happiness += 1
                print(f"{self.adadachi.name} loves playing {player_picks}!")

            if player_picks == self.inventory['games'][self.adadachi.hates_game()]:
                self.adadachi.happiness -= 1
                print(f"{self.adadachi.name} hates playing {player_picks}")
            print(f"{self.adadachi.name} played {player_picks}")
        else:
            print("Try again")

