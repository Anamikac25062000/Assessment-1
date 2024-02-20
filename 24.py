# 24) Write a Python program to calculate the sum of all elements in a list recursively.


def rec_sum(new):
    if not new:
        return 0
    else:
        return new[0]+rec_sum(new[1:])

list1=[6, 9, 10, 5, 2, 4]
result=rec_sum(list1)
print("Sum of elements recursively:", result)


