def fact(n):
    # Base case: 0! or 1! is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * fact(n - 1)

# Input from the user
num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is: {fact(num)}")