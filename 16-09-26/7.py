# Write a menu-driven python program where the user can add items, remove items, view cart, and exit

cart = []

while True:
    print("1.Add  2.Remove  3.View  4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        cart.append(input("Item: "))
    elif ch == "2":
        cart.remove(input("Item: "))
    elif ch == "3":
        print(cart)
    elif ch == "4":
        break
    else:
        print("Invalid choice")