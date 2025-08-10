def make_chai():
    # print("Here is your masala chai")
    return "ret Here is your masala chai"


return_value = make_chai()
# print(return_value)

def ideal_chaiwala():
    pass

# print(ideal_chaiwala())

def sold_Cups():
    return 120

total = sold_Cups()
# print(total)


def chai_status(cups_left):
    if cups_left == 0:
        return "sorry, chai over"
    return "chai is ready"
    print("chai")

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100, 20, 1000 # sold, remaining

sold, remaining, not_paid = chai_report()
print("Sold", sold)
print("remeaning", remaining)