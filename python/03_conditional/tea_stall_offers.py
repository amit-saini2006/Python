size_of_cup = input("what cup would you like to have: Small, Medium or Large: ").lower()

if size_of_cup == "small":
    print(f"{size_of_cup}! This size will cost 10 rupee")
elif size_of_cup == "medium":
    print(f"{size_of_cup}! This size will cost 15 rupee")
elif size_of_cup == "large":
    print(f"{size_of_cup}! This size will cost 20 rupee")
else:
    print(f"{size_of_cup}! This size is invalid")