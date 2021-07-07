shopping_cart = ["Apples", "Mangoes", "Bananas", "Stawberries"]

for item in shopping_cart:
    print(item)

print()

add_item = input("Enter the item in the cart: ").title()

shopping_cart.append(add_item)

remove_item = input("Enter the item you wish to remove from the cart: ").title()

shopping_cart.remove(remove_item)

print()

for item in shopping_cart:
    print(item)