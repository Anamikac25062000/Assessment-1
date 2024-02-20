# 9) Write a Python program to count the occurrences of an element in a list.


list1=[1, 1, 2, 2, 5, 4, 8, 8, 8, 9, 6, 7, 4]
count_elements=int(input("Enter the element"))
occurrences = list1.count(count_elements)
print(f"The element {count_elements} occurs {occurrences} times in the list.")
