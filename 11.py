# 11) Write a Python program to find the intersection of two lists.


list1 = [10, 20, 50, 40]
list2 = [30, 40, 20, 60]
intersection = []
for element in list1:
    if element in list2 and element not in intersection:
        intersection.append(element)
print("New intersected list:", intersection)

