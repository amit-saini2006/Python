# set

essential_speices = {'cardamon', 'ginger', 'cinnamon'}
optional_speices = {'cloves', 'ginger', 'black pepper'}

all_spices = essential_speices | optional_speices  # union in set | symbol
print(f"All spices: {all_spices}")

common_spices = essential_speices & optional_speices
print(f"Common spices: {common_spices}")

only_in_essential = essential_speices - optional_speices
print(f"Only in essentail species: {only_in_essential}")

print(f"Is 'cloves' in essential spices: {'cloves' in essential_speices}")