print("Welcome to Python Pizza Deliveries!")

small_size__pizza_price = 15
medium_size_pizza_price = 20
large_size_pizza_price = 25

pepperoni_price_small_pizza = 2
pepperoni_price_other_pizzas = 3

extra_cheese_price = 1

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    print("You have ordered Small size Pizza")
    bill += small_size__pizza_price
elif size == "M":
    print("You have ordered Medium size Pizza")
    bill += medium_size_pizza_price
elif size == "L":
    print("You have ordered Large size Pizza")
    bill += large_size_pizza_price
else:
    print("You entered wrong inputs!")

if pepperoni == "Y":
    print("You included pepperoni")

    if size == "S":
        bill += pepperoni_price_small_pizza
    else:
        bill += pepperoni_price_other_pizzas

if extra_cheese == "Y":
    print("You included extra cheese")
    bill += extra_cheese_price


print(f"Your final bill is : ${bill}.")
