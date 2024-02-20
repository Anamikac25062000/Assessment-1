# 15) Write a Python program to check if a string is an anagram of another string ("listen", "Silent")


string1=input("Enter a string:")
string2=input("Enter another string:")

if set(string1) == set(string2):
    print("The string1 is the anagram of string2")
else:
    print("The string1 is not the anagram of string2")
