print("Trip Cost Calculator")

km = float(input("Enter kilometers to drive: "))
fuel_usage = float(input("Enter liters-per-kilometer usage of the car: "))
fuel_price = float(input("Enter price per liter of fuel: "))

cost = (km / fuel_usage) * fuel_price

print(f'The trip cost is {cost}')