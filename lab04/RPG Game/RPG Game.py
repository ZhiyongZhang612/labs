# Item
class Item:
    def __init__(self, name, description="", rarity="common"):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ""

    def pick_up(self, character: str):
        self._ownership = character
        return f"{self.name} is now owned by {character}"

    def throw_away(self):
        self._ownership = False
        return f"{self.name} is thrown away."

    def use(self):
        if self._ownership:
            return f"{self.name} is used."
        return ""

# Weapon
class Weapon(Item):
    def __init__(self, name, damage, weapon_type, rarity="common"):
        Item.__init__(self, name, rarity=rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.15 if rarity == "legendary" else 1.0
        self.active = False

    def equip(self):
        if self._ownership:
            self.active = True
            return f"{self.name} is equipped by {self._ownership}."
        return f"{self.name} cannot be equipped without an owner."

    def use(self):
        if self.active and self._ownership:
            return f"{self.name} is used, dealing {self.damage * self.attack_modifier} damage."
        return ""

# Shield
class Shield(Item):
    def __init__(self, name, defense, broken=False, rarity="common"):
        Item.__init__(self, name, rarity=rarity)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.10 if rarity == "legendary" else 1.0
        self.broken_modifier = 0.5 if broken else 1.0
        self.active = False

    def equip(self):
        if self._ownership:
            self.active = True
            return f"{self.name} is equipped by {self._ownership}."
        return f"{self.name} cannot be equipped without an owner."

    def use(self):
        if self.active and self._ownership:
            defense_power = self.defense * self.defense_modifier * self.broken_modifier
            return f"{self.name} is used, blocking {defense_power} damage."
        return ""

# Potion
class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, rarity="common"):
        Item.__init__(self, name, rarity=rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    def use(self):
        if not self.empty and self._ownership:
            self.empty = True
            return f"{self._ownership} used {self.name}, {self.potion_type} increased by {self.value} for {self.effective_time}s"
        return ""

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        potion = cls(name=name, potion_type=potion_type, value=50, effective_time=30)
        potion.pick_up(owner)
        return potion

# Test
belthronding = Weapon(name='Belthronding', rarity='legendary', damage=5000, weapon_type='bow')
print(belthronding.pick_up('Beleg'))  # Belthronding is now owned by Beleg
print(belthronding.equip())  # Belthronding is equipped by Beleg
print(belthronding.use())  # Belthronding is used, dealing 5750 damage

broken_pot_lid = Shield(name='wooden lid', defense=5, broken=True)
print(broken_pot_lid.pick_up('Beleg'))  # wooden lid is now owned by Beleg
print(broken_pot_lid.equip())  # wooden lid is equipped by Beleg
print(broken_pot_lid.use())  # wooden lid is used, blocking 2.5 damage
print(broken_pot_lid.throw_away())  # wooden lid is thrown away
print(broken_pot_lid.use())  # NO OUTPUT because ownership is removed

attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', potion_type='attack')
print(attack_potion.use())  # Beleg used atk potion temp, and attack increase 50 for 30s
print(attack_potion.use())  # NO OUTPUT because the potion is now empty

print(isinstance(belthronding, Item))  # True
print(isinstance(broken_pot_lid, Shield))  # True
print(isinstance(attack_potion, Weapon))  # False
