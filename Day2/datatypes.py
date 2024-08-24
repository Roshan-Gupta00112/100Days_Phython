# Printing Different Data Types
import math

# 1. Numeric Data Type:- integer, float, Complex Number

# int
a = 123
print(type(a))

# float
b = 123.123456
print(type(b))

# complex
c = 3 + 7j
print(type(c))
d = 7j + 3
print(type(d))
if d == c:
    print("d and c both are the same.")
else:
    print("d and c are different.")


# 2. boolean Data Type
# bool
e = True
print(type(e))
f = False
print(type(f))



# 3. Dictionary Data Type
# dict
# # empty Dictionary
g = {}
print(type(g))

h = {
    "ARDM": ["Ahmed", "Horit", "Krishna", "Veera", "Roshan"]
}
print(type(h))



# 4. Set
# set
# empty set
i = set()
print(type(i))
#
j = {1, 2, 4, 'abc', True}
print(type(j))


# 5. Sequence Type:- String, Tuples, List

# String
# empty string
# str
k = ""
print(type(k))

l = "Roshan is a billionaire man"
print(type(l))

# Tuple
# tuple
# empty tuple
m = ()
print(type(m))

# single element tuple
n = (1, )
# # Note:- n = (1) -- It will be considered as a variable
print(type(n))
o = (1, "ty", True)
print(type(o))

# List
# empty list
p = []
print(type(p))

q = [1, "Billionaire"]
print(type(q))




