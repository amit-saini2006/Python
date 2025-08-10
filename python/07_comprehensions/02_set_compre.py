# syntax  --- {expression for item in iterable if condition}

favourite_chai = [
    "Masala Chai", "Green Tea", "Lemon Tea",
    "Masala Chai", "Lemon Tea"
]

unique_chai = {chai for chai in favourite_chai}
print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardmom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredents in recipes.values() for spice in ingredents}

print(unique_spices)