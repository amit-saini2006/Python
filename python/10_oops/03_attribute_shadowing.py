class Chai: 
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "small"
print("After changing",cutting.temperature)
print("Cup size is",cutting.cup)
print("Direct look into the class",Chai.temperature)

del cutting.temperature
print("After del temp",cutting.temperature)

del cutting.cup
# print("After del cup",cutting.cup)