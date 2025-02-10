# Basic menu ordering + total price calculation code


menu = {"item1": 3.00, 
        "item2": 4.50,
        "item3": 6.00,
        "item4": 2.50,
        "item5": 1.00,
        "item6": 3.50,
        "item7": 3.00,
        "item8": 4.25}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")