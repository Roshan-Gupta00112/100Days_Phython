print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where you want to go?")

step1 = input('Type "Left" or "Right"\n')

if step1.lower() == "left":
    print("River ahead. You want to swim or wait for boat?")

    step2 = input("Type Swim or Wait\n")

    if step2.lower() == "wait":
        print("There are 3 doors ahead. Inside which colour door you want to go, Red, Blue or Yellow?")

        step3 = input("Please type either Red or Blue or Yellow\n")

        if step3.lower() == "yellow":
            print("Congratulations! you got the treasure!\nYou Win!")
        elif step3.lower() == "red":
            print("Sorry, You Jumped into the fire and burnt.\nGame Over.")
        elif step3.lower() == "blue":
            print("Oh No! You eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")

    else:
        print("Attacked by trout.\nGame Over.")

else:
    print("Fall into a hole.\nGame Over.")
