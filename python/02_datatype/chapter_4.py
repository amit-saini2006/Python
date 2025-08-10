is_boiling = True
stic_count = 5
total_action = stic_count + is_boiling # upcasting
print(f'Total actions: {total_action}')

milk_present = 0 # None for zero
print(f'is there milk? {bool(milk_present)}')

water_hot = True
tea_added = False

can_serve = water_hot and tea_added # and, or, not
print(f'can serve chai? {can_serve}')