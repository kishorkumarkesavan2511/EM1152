def fb(n):
    print(f"Processing string: '{n}'")  # Debug statement to show the current string being proces
    # Base case: The first two Fibonacci numbers
    if n <= 1:
        return n
    # Recursive case: Sum of the two preceding terms
    return fb(n - 1) + fb(n - 2)

# Input from user
nt = int(input("Enter the position (n) for Fibonacci: "))

# Print the nth term in the Fibonacci series
print(f"The {nt}th term in the Fibonacci series is: {fb(nt)}")