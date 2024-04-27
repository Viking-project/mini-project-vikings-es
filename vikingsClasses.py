import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage 
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        
    def battleCry(self):
        return "Odin Owns You All!"        

    def receiveDamage(self, damage):
        self.health -= damage   #super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    
    

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
       super().__init__(health, strength)  

    def receiveDamage(self, damage):
        self.health -= damage   #super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"  

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if not self.vikingArmy:
            return "No vikings lefts"
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        message = saxon.receiveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return message
    
    def saxonAttack(self):
        if not self.saxonArmy:
            return "No saxons lefts"
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        fuerzaDeAtaque=saxon.attack()
        message = viking.receiveDamage(fuerzaDeAtaque)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return message

    def showStatus(self):
        if  len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

"""
pass 
#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass
"""
