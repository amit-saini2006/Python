def make_chai():
    if ketle_is_empty():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        clean_cup()
    add_to_cup("tea_leaves")
    add_to_cup("sugar")
    pour('boiled_water')
    stir('cup')
    serve('chai')

make_chai()