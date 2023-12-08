import random

Player_Health = 100
enemy_health = 100
inventory = []

def attack_enemy(Player_Health, enemy_health):
    while True:
        if Player_Health > 0:
            your_attack = random.randint(10, 100)
            print(f"You attacked your enemy for {your_attack} damage!")
            enemy_health -= your_attack
        
        if enemy_health > 0:
            enemy_attack = random.randint(10, 100)
            print(f"the enemy attacked you for {enemy_attack} damage!")
            Player_Health -= enemy_attack 
        
        if Player_Health <= 0:
            print("You are tasty you are not getting away dinner!!")
            exit()

        elif enemy_health <= 0:
            print("I now have the urge to eat him.")
            print("You recived 25 health and an item in your invetory from eating your attacker")
            Player_Health += 25
            inventory.append("sword")
            break

def enemy_attacks_you(Player_Health, enemy_health):
    while True:
        if enemy_health > 0:
            enemy_attack = random.randint(10, 100)
            print(f"the enemy attacked you for {enemy_attack} damage!")
            Player_Health -= enemy_attack 
        
        if Player_Health > 0:
            your_attack = random.randint(10, 100)
            print(f"You attacked your enemy for {your_attack} damage!")
            enemy_health -= your_attack
        
        if Player_Health <= 0:
            print("You are tasty you are not getting away dinner!!")
            exit()

        elif enemy_health <= 0:
            print("I now have the urge to eat him.")
            print("You recived 25 health and an item in your invetory from eating your attacker")
            Player_Health += 25
            inventory.append("sword")
            break


Name = input("Hello dinn- I mean hello weary traveler welcome to my tropical island. what is your name?  ")
print(f"Hello {Name} Before you go out hunting monsters for me I need all you to sign relase forms for in the case you don't come back and I need all your personal information. ")
print("Thanks for giving me your signing and giving all your personal information. You need to go hunt the monsters off my bermuda triangle where none return. ")
while True:
    user_input_one = input("Press w to be eat- I mean to walk Press i to check to see if you can be cook- I mean to check your inventory and health. ")
    if user_input_one == "w":
        print("You moved one foot with your feet")
        chance = random.randint(1,2)
        if chance == 2:
            enemy_chance = random.randint(1, 3)
            if enemy_chance == 1:
                print("You ran into a zombie")
            if enemy_chance == 2:
                print("You ran into cannible Nazises")
            if enemy_chance == 3:
                print("You ran into a uncontacted cannible tribe")
            attack_choice = input("Would you like to attack or run: a or r")
            if attack_choice == "a":
                attack_enemy(Player_Health, enemy_chance)
            elif attack_choice == "r":
                run_chance = random.randint(1,2)
                if run_chance == 1:
                    enemy_attacks_you(Player_Health, enemy_health)
                else:
                    print("You got away!")
    elif user_input_one == "i":
        print(f"You have {Player_Health} health left and you have {inventory} in your inventory")