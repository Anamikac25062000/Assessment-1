# 22) Write a Python program to check if a given number is a perfect number.


def pfct_number(num):
    if num<=0:
        return False

    sum_of_divisor=0

    for divisor in range(1, num):
        if num % divisor==0:
            sum_of_divisor += divisor

    return sum_of_divisor==num
input_num = int(input("Enter a number: "))

if pfct_number(input_num):
    print(input_num, "is a perfect number.")
else:
    print(input_num, "is not a perfect number.")

