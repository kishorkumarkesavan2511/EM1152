#Program – Swapping Two Numbers
#  Get input from the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# Swap the numbers using multiple assignment
a, b = b, a
print("After swapping:")
print("First number:", a)
print("Second number:", b)
