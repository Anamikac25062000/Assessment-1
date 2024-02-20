# 25) Write a Python program to count the number of occurrences of each element in a tuple.


tuple1=(1, 2, 3, 1, 3, 5, 9, 6, 1, 9)
occurrence={}

for element in tuple1:
    if element in occurrence:
        occurrence[element]+=1
    else:
        occurrence[element]=1
print(occurrence)

