# len function
list1 = [1, 2, 3, 4, 1, 5, 6, 7, 8, 9, 1]
print(len(list1))
print(list1)

# 1. Appending or adding an item at the end
list1.append(10)
print(f"Length of a list after appending an item is: {len(list1)}")
print(list1)

# 2. Extending or adding a list of items into another list
list1.extend([11, 12, 14])
print(f"Length of a list after extending it is: {len(list1)}")
print(list1)

# 3. Inserting an item at a specific index
list1.insert(0, 0.0)
print(f"Length of a list after inserting an item at mentioned index is: {len(list1)}")
print(list1)

# 4. Getting count of an item
count_val = list1.count(1)
print(f"Count of 1 in list is: {count_val}")
print(len(list1))
print(list1)

# 5. a. Sorting the list in ascending order
list1.sort()
print(f"Length of list after sorting it is: {len(list1)}")
print(list1)

# 5. b. Sorting the List in Reverse order
list1.sort(reverse=True)
print(f"Length of list after sorting it in reverse order is: {len(list1)}")
print(list1)

# 6. Reversing the List
list1.reverse()
print(f"Length of list after reversing it's items is: {len(list1)}")
print(list1)

# 7. Creating copy of a list
list2 = list1.copy()
print(f"Length of the copied list from the original list is: {len(list2)}")
print(list2)

# 8. Removing the first occurrence of a mentioned item
list1.remove(1)
print(f"Length of the list after removing mentioned item is: {len(list1)}")
print(list1)

# 9. Popping the item from the mentioned index
popped_val = list1.pop(4)
print(f"Popped out value is: {popped_val}")
print(len(list1))
print(list1)

# 10. Getting the first index of the item between the two indices
index_val = list1.index(1, 0, 9)
print(f"First occurrence Index of the mentioned item between the mentioned position is: {index_val}")
print(len(list1))
print(list1)

# 11. Clearing or Removing all items from the list
list1.clear()
print(f"Length of the list after clearing or removing it's all items is: {len(list1)}")
print(list1)
