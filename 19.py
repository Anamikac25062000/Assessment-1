#  19) Write a Python program to count the number of vowels in a string.


vowels=['a', 'e', 'i', 'o', 'u']
str=input("Enter a string:")
count=0
str_lower=str.lower()
for character in str_lower:
    if character in vowels:
        count += 1
print("Number of vowels in the string:", count)


