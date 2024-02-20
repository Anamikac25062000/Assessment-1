# 16) Write a Python program to merge two sorted lists into a single sorted list.

list1 = [1, 2, 10, 1, 3, 4]
list2 = [3, 1, 2, 10, 5, 7]

list1.sort()
list2.sort()

added_list = list1 + list2
without_duplicates = list(set(added_list))
added_list = sorted(without_duplicates)

print("List 1:", list1)
print("List 2:", list2)
print("Merged List without Duplicates:", without_duplicates)
print("Final Sorted List:", added_list)
