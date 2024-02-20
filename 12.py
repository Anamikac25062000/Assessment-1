# 12) Write a Python program to flatten a nested list. ([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])

def flatten(lst):
    result = []

    for i in lst:
        if type(i) is list:
            result.extend(flatten(i))
        else:
            result.append(i)

    return result

nested_list = [2, [[3, 4], 6, 7], 10, [8, 10]]
flattened_list = flatten(nested_list)
print(flattened_list)
