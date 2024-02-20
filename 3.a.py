# 3) print the following patterns:
# a.

# 0

# 00

# 000

# 0000

for row in range(1,5):
    for col in range(row):
        print(0,end="")
    print()