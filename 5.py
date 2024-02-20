# 5) Write a Python program to implement a stack using a list. (push and pop)


stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after pushing 1, 2, and 3:", stack)

if stack:
    popped_item = stack.pop()
    print("Popped item:", popped_item)
else:
    print("Stack is empty. Cannot pop.")

print("Stack after popping:", stack)

# Peek at the top element without removing it
if stack:
    peeked_item = stack[-1]
    print("Peeked item:", peeked_item)
else:
    print("Stack is empty. Cannot peek.")

print("Size of the stack:", len(stack))
