# 13) Write a Python program to check if a string contains only digits. ("12345"-->True)

i = input("Enter a string:")

for digit in i:
    if digit.isnumeric():
        continue
    else:
        print(False)
        break
else:
    print(True)
