users = [
    {"id": 1, "total": 100, "coupon": "o20"},
    {"id": 2, "total": 120, "coupon": "p40"},
    {"id": 3, "total": 60, "coupon": "f10"},
]

discounts = {
    "o20": (0.2, 0),
    "p40": (0.5, 0),
    "f10": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")