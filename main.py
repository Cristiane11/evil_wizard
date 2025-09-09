# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.evade_next = False # created evade attribute
        self.shield_next = False # created shield attribute 
          

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if opponent.evade_next:
            print(f"{opponent.name} evades the attack!")
            opponent.evade_next = False
            return
        if opponent.shield_next:
            damage //= 2
            opponent.shield_next = False
            print(f"{opponent.name} blocks the attack with a shield!")
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")




    #Creted the heal
    def heal(self):
        heal_amount = 20
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")   

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
    # Optionally, add a special ability method here 
    def special_ability(self, opponent):
        # Example for Archer: double attack
        opponent.health -= self.attack_power * 2
        print(f"{self.name} uses Double Shot on {opponent.name} for {self.attack_power * 2} damage!")
    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")
# Create Paladin class 
class Paladin(Character):   
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
    # Optionally, add a special ability method here 
    def special_ability(self, opponent):
        # Example for Paladin: shield (reduce next attack damage by half)
        self.shield_next = True
        print(f"{self.name} uses Shield! Next attack damage will be reduced by half.")
    def holy_strike(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Implement Archer class
    elif class_choice == '4':
        return Paladin(name)  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Special Ability 2")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                player.special_ability(wizard)  
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
            else:
                print("Your class does not have Special Ability 1.")
        elif choice == '3':
            if isinstance(player, Archer):
                player.evade()
            elif isinstance(player, Paladin):
                player.special_ability(wizard)  # Shield
            else:
                print("Your class does not have Special Ability 2.")
        elif choice == '4':
            player.heal()
        elif choice == '5':                  
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

