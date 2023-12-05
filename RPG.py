import random

Player_Health = 100
enemy_health = 100
def attack_enemy(Player_Health, enemy_health):
     while True:
          if Player_Health > 0:
            your_attack = random.randint(10, 100)
            print(f"You attacked your enemy for {your_attack} damage!")
            enemy_health -= your_attack
        
            if enemy_health > 0:

dead = False


Name = input("Hello dinn- I mean hello weary traveler welcome to my tropical island. what is your name?  ")
print(f"Hello {Name} Before you go out hunting monsters for me I need all you to sign relase forms for in the case you don't come back and I need all your personal information. ")
print("Thanks for giving me your signing and giving all your personal information. You need to go hunt the monsters off my bermuda triangle where none return. ")
while dead == False:
    user_input_one = input("Press w to be eat- I mean to walk Press i to check to see if you can be cook- I mean to check your inventory and health. ")
    if user_input_one == "w":
            print("You moved one foot with your feet")
            chance = random.randint(0,3)
            if chance == 3:
               pass  
    if user_input_one == "i":
        pass #put invantory code here
    else:
        print("unsurported input")
