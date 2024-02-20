# 18) Write a Python program to find the second largest number in a list.


list1=[2, 8, 9, 4]
larger_element= max(list1)
list1.remove(larger_element)
second_largest=max(list1)
print("second largest number in the list is",second_largest)