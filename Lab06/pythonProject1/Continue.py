import json
# Item class
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

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'ownership': self._ownership
        }

    @classmethod
    def from_json(cls, data):
        item = cls(name=data['name'], description=data['description'], rarity=data['rarity'])
        item._ownership = data.get('ownership', "")
        return item

    def __str__(self):
        return f"{self.name} ({self.rarity}) - {self.description}"


# Weapon base class
class Weapon(Item):
    def __init__(self, name, damage, weapon_type, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.15 if rarity == "legendary" else 1.0
        self.active = False

    def equip(self):
        if self._ownership:
            self.active = True
            return f"{self.name} is equipped by {self._ownership}."
        return f"{self.name} cannot be equipped without an owner."

    def attack_move(self):
        return f"{self.name} performs a basic attack."

    def use(self):
        if self.active and self._ownership:
            return f"{self.name} is used, dealing {self.damage * self.attack_modifier} damage."
        return ""

    def __str__(self):
        if self.rarity == "legendary":
            return f"Legendary Weapon: {self.name} Damage: {self.damage} Type: {self.weapon_type}"
        else:
            return super().__str__()

    def to_json(self):
        data = super().to_json()
        data.update({
            'type': 'Weapon',
            'damage': self.damage,
            'weapon_type': self.weapon_type,
            'active': self.active
        })
        return data

    @classmethod
    def from_json(cls, data):
        weapon = cls(name=data['name'], damage=data['damage'], weapon_type=data['weapon_type'], rarity=data['rarity'])
        weapon.active = data.get('active', False)
        weapon._ownership = data.get('ownership', "")
        return weapon


# SingleHandedWeapon subclass
class SingleHandedWeapon(Weapon):
    def attack_move(self):
        return f"{self.name} performs a slashing attack!"

    def to_json(self):
        data = super().to_json()
        data.update({'type': 'SingleHandedWeapon'})
        return data

    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], damage=data['damage'], weapon_type=data['weapon_type'], rarity=data['rarity'])


# DoubleHandedWeapon subclass
class DoubleHandedWeapon(Weapon):
    def attack_move(self):
        return f"{self.name} spins and delivers a powerful blow!"

    def to_json(self):
        data = super().to_json()
        data.update({'type': 'DoubleHandedWeapon'})
        return data

    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], damage=data['damage'], weapon_type=data['weapon_type'], rarity=data['rarity'])


# Pike subclass
class Pike(Weapon):
    def attack_move(self):
        return f"{self.name} thrusts forward with deadly precision!"

    def to_json(self):
        data = super().to_json()
        data.update({'type': 'Pike'})
        return data

    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], damage=data['damage'], weapon_type=data['weapon_type'], rarity=data['rarity'])


# RangedWeapon subclass
class RangedWeapon(Weapon):
    def attack_move(self):
        return f"{self.name} shoots a precise arrow!"

    def to_json(self):
        data = super().to_json()
        data.update({'type': 'RangedWeapon', 'ammo': getattr(self, 'ammo', None)})
        return data

    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], damage=data['damage'], weapon_type=data['weapon_type'], rarity=data['rarity'])


# Shield class
class Shield(Item):
    def __init__(self, name, defense, broken=False, rarity="common"):
        super().__init__(name, rarity=rarity)
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

    def to_json(self):
        data = super().to_json()
        data.update({
            'type': 'Shield',
            'defense': self.defense,
            'broken': self.broken,
            'active': self.active
        })
        return data

    @classmethod
    def from_json(cls, data):
        shield = cls(name=data['name'], defense=data['defense'], broken=data['broken'], rarity=data['rarity'])
        shield.active = data.get('active', False)
        shield._ownership = data.get('ownership', "")
        return shield


# Potion class
class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, rarity="common"):
        super().__init__(name, rarity=rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    def use(self):
        if not self.empty and self._ownership:
            self.empty = True
            return f"{self._ownership} used {self.name}, {self.potion_type} increased by {self.value} for {self.effective_time}s"
        return ""

    def to_json(self):
        data = super().to_json()
        data.update({
            'type': 'Potion',
            'potion_type': self.potion_type,
            'value': self.value,
            'effective_time': self.effective_time,
            'empty': self.empty
        })
        return data

    @classmethod
    def from_json(cls, data):
        potion = cls(name=data['name'], potion_type=data['potion_type'], value=data['value'], effective_time=data['effective_time'], rarity=data['rarity'])
        potion.empty = data.get('empty', False)
        potion._ownership = data.get('ownership', "")
        return potion

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        potion = cls(name=name, potion_type=potion_type, value=50, effective_time=30)
        potion.pick_up(owner)
        return potion
# Inventory class
class Inventory:
    def __init__(self, owner=None):
        self.items = []
        self.owner = owner

    def add_item(self, item):
        item.pick_up(self.owner)
        self.items.append(item)

    def remove_item(self, inv_item):
        if inv_item in self.items:
            inv_item.throw_away()
            self.items.remove(inv_item)

    def view(self, item_type=None):
        if item_type:
            return [str(inventory_entry) for inventory_entry in self.items if isinstance(inventory_entry, item_type)]
        else:
            return [str(inventory_entry) for inventory_entry in self.items]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, inv_item):
        return inv_item in self.items

    def to_json(self):
        return {
            'owner': self.owner,
            'items': [item.to_json() for item in self.items]
        }

    @classmethod
    def from_json(cls, data):
        inventory = cls(owner=data.get('owner'))
        for item_data in data['items']:
            if item_data['type'] == 'Shield':
                inventory.add_item(Shield.from_json(item_data))
            elif item_data['type'] == 'Potion':
                inventory.add_item(Potion.from_json(item_data))
            elif item_data['type'] == 'SingleHandedWeapon':
                inventory.add_item(SingleHandedWeapon.from_json(item_data))
            elif item_data['type'] == 'DoubleHandedWeapon':
                inventory.add_item(DoubleHandedWeapon.from_json(item_data))
            elif item_data['type'] == 'Pike':
                inventory.add_item(Pike.from_json(item_data))
            elif item_data['type'] == 'RangedWeapon':
                inventory.add_item(RangedWeapon.from_json(item_data))
        return inventory


# Function for serialization
def inventory_to_json(obj):
    if isinstance(obj, Inventory):
        return obj.to_json()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")



# Test Code
if __name__ == "__main__":
    master_sword = SingleHandedWeapon(name="Master Sword", rarity="legendary", damage=300, weapon_type="sword")
    muramasa = DoubleHandedWeapon(name="Muramasa", rarity="legendary", damage=580, weapon_type="katana")
    gungnir = Pike(name="Gungnir", rarity="legendary", damage=290, weapon_type="spear")
    belthronding = RangedWeapon(name="Belthronding", rarity="legendary", damage=500, weapon_type="bow")

    broken_pot_lid = Shield(name="Broken Pot Lid", defense=5, broken=True)
    round_shield = Shield(name="Round Shield", defense=100, broken=False)
    hp_potion = Potion(name="Health Potion", potion_type="HP", value=100)

    beleg_backpack = Inventory(owner="Beleg")
    beleg_backpack.add_item(belthronding)
    beleg_backpack.add_item(hp_potion)
    beleg_backpack.add_item(master_sword)
    beleg_backpack.add_item(broken_pot_lid)
    beleg_backpack.add_item(muramasa)
    beleg_backpack.add_item(gungnir)
    beleg_backpack.add_item(round_shield)

    print("Viewing shields in the inventory:", beleg_backpack.view(item_type=Shield))

    print("Viewing all items in the inventory:", beleg_backpack.view())

    beleg_backpack.remove_item(broken_pot_lid)

    print("Inventory after removing Broken Pot Lid:", beleg_backpack.view())

    if master_sword in beleg_backpack:
        master_sword.equip()
        print(master_sword)
        print(master_sword.use())

    # Serialize to JSON
    with open('inventory.json', 'w') as file:
        json.dump(beleg_backpack, file, default=inventory_to_json)

    # Deserialize from JSON
    with open('inventory.json', 'r') as file:
        data = json.load(file)
        new_inventory = Inventory.from_json(data)

    print("Deserialized inventory:", new_inventory.view())