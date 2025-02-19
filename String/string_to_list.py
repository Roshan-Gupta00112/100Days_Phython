str1 = "billionaire"
list1 = list(str1)
print(list1)
print(list1[0])



str2 = " "
list2 = list(str2)
print(list2)
print(list2[0])


str3 = ""
list3 = list(str3)
print(list3)

print(list3[0])
# Error
# print(list3[0])
#           ~~~~~^^^
# IndexError: list index out of range

# Because list3 is an empty list which means there is no element inside it.
