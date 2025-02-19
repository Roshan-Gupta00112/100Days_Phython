import os
import sys

# Not Worked when try to clear phycharm console
def clear_console():
    if sys.platform == "win32":
        os.system("cls")  # Windows
    else:
        os.system("clear")  # Linux/Mac

# Test the function
print("Billionaire\n"*5)
clear_console()
print("Console cleared!")