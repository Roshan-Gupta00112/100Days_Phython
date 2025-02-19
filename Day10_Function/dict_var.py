add = 5
subtract = 6
multiply = 7
divide = 8


dict_operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



# 1st Approach: - For Printing
# for key in dict_operator:
#     print(f"{key}: {dict_operator[key]}")


# 2nd Approach: - For Printing
# for key in dict_operator:
#     print(f"{key}: {dict_operator.get(key)}")



# 3rd Approach: - For Printing
for key, val in dict_operator.items():
    print(f"{key}: {val}")