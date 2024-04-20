import random
from vikingsClasses import Viking, Saxon, War

def create_vikings():
    names = ["Javier", "Meg", "Diego", "Criiis"]
    name = random.choice(names)
    health = random.randint(1,300)
    strength = random.randint(1,300)
    return Viking(name, health, strength)

def create_saxon():
    health = random.randint(1,150)
    strength = random.randint(1,150)
    return Saxon(health, strength)

def create_teams(num_vikings, num_saxons):
    war = War
    for _ in range(num_vikings):
        war.addViking(create_vikings())
    
    for _ in range(num_saxons):
        war.addSaxon(create_saxon())
    
    return war
    

def play_game():
    war = create_teams(10, 10)
    while war.showStatus != "Vikings and Saxons are still in the thick of battle.":
        if random.choice([True, False]):
            result = war.vikingAttack()
        else:
            result = war.saxonAttack()
        print(result)
        print(war.showStatus)

    

play_game()