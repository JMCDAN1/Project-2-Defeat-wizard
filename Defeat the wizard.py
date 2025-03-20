# Base Character class
import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability_1(self, wizard):
        print(f"{self.name} uses Special Ability: Twin Flame")
        damage = random.randint(65, 75)
        wizard.health -= damage
        print(f"{self.name} deals {damage} damage with Twin Flame")

    def special_ability_2(self, wizard):
        print(f"{self.name} uses Special Ability: Iron Slice")
        damage = random.randint(40, 50)
        wizard.health -= damage
        print(f"{self.name} deals {damage} damage with Iron Slice!")


    def heal(self):
        heal_amount = random.randint(40, 50)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} points!  Their Current health is: {self.health}")



# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability_1(self, wizard):
        print(f"{self.name} uses Special Ability: Steel Ball")
        damage = random.randint(70, 80)
        wizard.health -= damage
        print(f"{self.name} hits for {damage} damage with Steel Ball")

    def special_ability_2(self, wizard):
        print(f"{self.name} uses Special Ability: Chain Link")
        damage = random.randint(60, 65)
        wizard.health -= damage
        print(f"{self.name} deals {damage} damage with Chain Link")


    def heal(self):
        heal_amount = random.randint(30, 50)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} points!  Their Current health is: {self.health}")



#Ninja Class
class Ninja(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=55)


    def special_ability_1(self, wizard):
        print(f"{self.name} uses Special Ability: Silent Slash")
        damage = random.randint(77, 87)
        wizard.health -= damage
        print(f"{self.name} hits for {damage} damage with Silent Slash")

    def special_ability_2(self, wizard):
        print(f"{self.name} uses Special Ability: Shadow Blade")
        damage = random.randint(55, 70)
        wizard.health -= damage
        print(f"{self.name} hits for  {damage} damage with Shadow Blade")


    def heal(self):
        heal_amount = random.randint(20, 50)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} points!  Their Current health is: {self.health}")



#Huntewr Class
class Hunter(Character):
    def __init__(self, name):
        super(). __init__(name, health=200, attack_power=90)

    
    def special_ability_1(self, wizard):
        print(f"{self.name} uses Special Ability: Guided Arrow")
        damage = random.randint(80, 90)
        wizard.health -= damage
        print(f"{self.name} hits for {damage} damage with Guided Arrow")

    def special_ability_2(self, wizard):
        print(f"{self.name} uses Special Ability: Arrow Of Regret")
        damage = random.randint(65, 85)
        wizard.health -= damage
        print(f"{self.name} hits for {damage} damage with Arrow Of Regret")


    def heal(self):
        heal_amount = random.randint(50, 50)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} points!  Their Current health is: {self.health}")



# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

#Characters to choose from
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Ninja") 
    print("4. Hunter")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Ninja(name)  
    elif class_choice == '4':
        return Hunter(name)  
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            print("1. Special ability 1")
            print("2. Special ability 2")
            ability_choice = input("choose special ability")

            if ability_choice == '1':
                player.special_ability_1(wizard)
            elif ability_choice == '2':
                player.special_ability_2(wizard)
        elif choice == '3':
            player.heal()  
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()