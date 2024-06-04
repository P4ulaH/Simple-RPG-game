import random as rand   

class Player: 
    
   def __init__(self, name, health, points):
      self.name = name
      self.health = health
      self.points = points
   
class Monster:
    def __init__(self, name, health, attack_min, attack_max, points):
        self.name = name
        self.health = health
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.points = points

    def get_attack(self):
        return rand.randint(self.attack_min, self.attack_max)
     

Shadowflame = Monster("Shadowflame", 30, 10, 30, 20)
Frostpire = Monster("Frostpire", 50, 20, 50, 35)
Draconian = Monster("Draconian", 100, 60, 100, 80)
         

        
player_name = input("\nEnter your epic battle name=> ")
player = Player(player_name, 200, 0)

print("\nHey,", player.name, "ready for a battle? Here are the rules: ")
print("  - type 'r' to run or 'a' to attack")
print("  - at the start you have 200 health and 0 points")
print("  - each monster has a different amount of health and attack and it can attack you in these ranges:")
print("     - Shadowflame: 10-30, 20 points")
print("     - Frostpire: 20-50, 35 points")
print("     - Draconian: 60-100, 80 points")
print("  - you can heal yourself by buying food in the shop with the points you earn in the battle")
print("  - type stats to see your status and what is available in the shop:")
print("     - Moonberry = 60 points, heals 60 health")
print("     - Stardust Muffin = 100 points, heals 100 health")
print("     - Frostbite Delight = 200 points, heals 200 health")
print("  - type the name of the food you want to buy, to buy it")
print("  - type exit to exit the game")
print("  - don't worry about capitalization")
print("  - Enjoy the game and try to not die!")

monsters = [Shadowflame, Frostpire, Draconian]


#game loop
while player.health > 0:
   
   monster = rand.choice(monsters)
   print("\nYou have encountered a", monster.name)
   RorA = input("Do you want to (r)un or (a)ttack? ")
   RorA = RorA.lower()
   
   if RorA == "r":
      print("You ran away")
      continue
   elif RorA == "a":
      print("You attacked the", monster.name)
      player.health -= monster.get_attack()
      print("\nThe", monster.name, "attacked you and you now have", player.health, "health")
      if player.health <= 0:
         print("You died")
         break
      else:
         player.points += monster.points
         print("You now have", player.points, "points")
         print("The monster attacked you with", monster.get_attack(), "damage")
         print("You defeated the", monster.name, "!!!")
         continue
   elif RorA == "stats":
      print("\nYou have", player.points, "points")
      print("You have", player.health, "health")
      print("You can buy:")
      print("Moonberry = 60 points, heals 60 health")
      print("Stardust Muffin = 100 points, heals 100 health")
      print("Frostbite Delight = 200 points, heals 200 health")
      continue
   elif RorA == "moonberry":
      if player.points >= 60:
         player.health += 60
         player.points -= 60
         print("\nYou just bought a Moonberry!")
         print("You now have", player.health, "health")
         print("You now have", player.points, "points")
         continue
      else:
         print("You don't have enough points")
         continue
   elif RorA == "stardust muffin":
      if player.points >= 100:
         player.health += 100
         player.points -= 100
         print("\nYou just bought a Stardust Muffin!")
         print("You now have", player.health, "health")
         print("You now have", player.points, "points")
         continue
      else:
         print("You don't have enough points")
         continue
   elif RorA == "frostbite delight":
      if player.points >= 200:
         player.health += 200
         player.points -= 200
         print("\nYou just bought a Frostbite Delight!")
         print("You now have", player.health, "health")
         print("You now have", player.points, "points")
         continue
      else:
         print("You don't have enough points")
         continue
   elif RorA == "exit":
      break
   else:
      if_exit = input("That is not a valid option. Do you want to exit? yes/no ")
      if_exit = if_exit.lower()
      if if_exit == "yes":
         break
      else:
         continue