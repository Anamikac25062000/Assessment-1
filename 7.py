# 7) Write a Python program to implement a binary search on a sorted list.

sorted_list=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
element=19

low_index, high_index = 0, len(sorted_list) - 1
found = False

while low_index <= high_index:
    mid_index = (low_index + high_index) // 2
    mid_element = sorted_list[mid_index]

    if mid_element == element:
        found = True
        break
    elif mid_element < element:
        low_index = mid_index + 1
    else:
        high_index = mid_index - 1

if found:
    print(element, "found at index", mid_index)
else:
    print(element, "not found in the list.")
