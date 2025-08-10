# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing",order)

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]
def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") 
make_chai(tea="Green", sugar="Medium", milk="No")

def specail_chai(*ingredients, **extras):
    print("Ingridents", ingredients)
    print("extras", extras)

specail_chai("Cinnamon", "cardmom", sweetener="Honey", foam="yes")

# def chai_orders(order=[]):
#     order.append("Masala")
#     print(order)


def chai_orders(order=None):
    if order is None:
        order = []
    print(order)

chai_orders()
chai_orders()