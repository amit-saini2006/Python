# List   // Mutable

ingridents = ['water', 'milk', 'black tea']

ingridents.append('sugar')
print(f'Ingridents are: {ingridents}')

ingridents.remove('water')
print(f'Ingridents are: {ingridents}')

spice_option = ["ginger", "cardamom"]
chai_ingridients = ["water", "milk"]

chai_ingridients.extend(spice_option)
print(f"chai: {chai_ingridients}")

chai_ingridients.insert(2, "black tea")
print(f"chai: {chai_ingridients}")

last_added = chai_ingridients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingridients}")

chai_ingridients.reverse()
print(f"chai: {chai_ingridients}")

chai_ingridients.sort()
print(f"chai: {chai_ingridients}")

sugar_levels = [1,2,3,4,5]
print(f"Max sugar lvl: {max(sugar_levels)}")
print(f"Min sugar lvl: {min(sugar_levels)}")

base_liquid = ['water', 'milk']
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Bytes: {raw_spice_data}")