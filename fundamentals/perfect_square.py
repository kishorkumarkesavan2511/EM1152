# This program finds all perfect squares up to a given number n

# Get the number n from the user
n = int(input("Enter the number up to which you want to find perfect squares: "))

# Use list comprehension to find all perfect squares up to n
ps = [x * x for x in range(1, int(n ** 0.5) + 1) if x * x <= n]

# Print the perfect squares
print("Perfect squares up to", n, "are:", *ps)
