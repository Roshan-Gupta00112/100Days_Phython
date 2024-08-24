# Cannot use Length(len) function for Numeric or Boolean Data Types.

# print(len(1234))
# # TypeError: object of type 'int' has no len()

# print(len(True))
# # TypeError: object of type 'bool' has no len()


# print(len('1234'))

# We cane use underscore between numbers for the larger numbers
# print(1234567890)
# print(1_23_456_7_890)
# print(1_2_3_45_6_7_89_0_32595_839)
# print(98_76_54_321)
# print(987_654_321)
#
# c = 98_76_54_321
# d = 987_654_321
# if c == d:
#     print("Both numbers are same!")


# a = 123
# b = "123"

# print(type(a))
# # <class 'int'>
#
# print(type(b))
# # <class 'str'>


# DIVISION:-
# Division gives a float data type as an output
# To get the floor value(smaller nearest integer value for a division we need to use 2 forward slash instead of 1 which
# we use for division to get the floor value)

# print(5/2)
# # 2.5
# # floor Division
# print(5//2)
# # 2
#
# print(14/5)
# # 2.8
# print(14//5)
# # 2




# ROUND
# 1. Using round function
print(round(14/5, 2))
# 2.8

# 2. Using Format function
print("{:.2f}".format(14/5))
# 2.80
