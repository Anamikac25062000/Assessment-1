# 17) Write a Python program to find the sum of all even numbers in a list.


list1=[10, 7, 20, 4, 5, 9]
sum=0
for element in list1:
    if element%2==0:
        sum=sum+element
print(sum)
