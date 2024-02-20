# 23) Write a Python program to find the GCD (Greatest Common Divisor) of two numbers. (gcd(48, 60)=12)


num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
gcd=1
for i in range(1,(num1+1)):
    if ((num1%i==0)&(num2 % i==0)):
        gcd=i
print(gcd)