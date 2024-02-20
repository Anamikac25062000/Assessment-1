# 2)Write a program to check the validity of a password. Primary conditions for password validation:

# -minimum 8 charecters-The alphabet must be between [a-z]-At least one alphabet should be of Upper Case [A-Z]
# -At least 1 number or digit between [0-9].-At least 1 character from or @ or $1.

# Examples:Input: R@m@_fortuges Output: Valid Password
# Input: Rama fortunes Output: Invalid Password Explanation: Number is missing
# Input: Rama#fortule 
# Output: Invalid Password Explanation: Must consist from or@or $


password = input("Enter a password:")

if len(password) < 8:
    print("Password is Invalid, must contain minimum 8 characters.")
elif not any(char.islower() for char in password):
    print("Password is Invalid, the alphabet must be between [a-z].")
elif not any(char.isupper() for char in password):
    print("Password is Invalid, at least one alphabet should be of Upper Case.")
elif not any(char.isdigit() for char in password):
    print("Password is Invalid, number is missing.")
elif not any(char in ('@', '_', '$') for char in password):
    print("Password is Invalid, Must consist of _ or @ or $.")
else:
    print("Password is Valid")
