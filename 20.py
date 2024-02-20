# 20) Write a Python program to remove all occurrences of a given element from a list.

list1 = [1, 2, 3, 3, 5, 6, 8, 8, 3, 2, 9] 
element = input("Choose an element from the list: ")

element = int(element)

if element in list1:
    while element in list1:
        list1.remove(element)

print("List after removing all occurrences of", element, "is", list1)

                # OR

# list1 = [1, 2, 3, 3, 5, 6, 8, 8, 3, 2, 9] 
# element = input("Choose an element from the list: ")

# element = int(element)

# list1 = [item for item in list1 if item!=element]
# print("List after removing all occurrences of", element, "is", list1)
