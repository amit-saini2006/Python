chai_menu = {"Masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exists")

print("hello there...")