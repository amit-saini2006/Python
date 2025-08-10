def infy_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infy_chai()
user2 = infy_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))