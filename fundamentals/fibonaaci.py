# Get the number of terms from the user
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Initialize the first two terms of the Fibonacci series
f1, f2 = 2, 3

# Generate Fibonacci series using a for loop
for i in range(n):
    print(f1, end =" ")
    f1, f2 = f2, f1+f2
