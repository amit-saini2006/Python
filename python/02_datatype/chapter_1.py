sugar_amount = 2
print(f"Initial Sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial Sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# Both are inmutable means inchangable 
# There is only change in refernce not the value
# By changing the value we created a seprate id which exist with prev id
# It does not overwrite the value it just make another value with different id
