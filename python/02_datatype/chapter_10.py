# dictionary 

chai_order = dict(type="masala chai", size ="large", sugar = 2)
print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"recipe base: {chai_recipe['base']}")

print(f"recipe: {chai_recipe}")
del chai_recipe['liquid']
print(f"recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = dict(type="ginger chai", size ="medium", sugar = 1)

# print(f"order details (keys): {chai_order.keys()}")
# print(f"order details (values): {chai_order.values()}")
# print(f"order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {'cardamon': "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"updated chai recipe: {chai_recipe}")

chai_note = chai_order.get("note", "No note")
print(f"Chai size is: {chai_note}") 