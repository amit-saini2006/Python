# syntax  --- (expression for item in iterable if condition)

daily_sales = [5, 10, 15, 2, 3, 8, 9, 19]

total_cups = sum(sales for sales in daily_sales if sales > 5)

print(total_cups)