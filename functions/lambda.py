from functools import reduce  # Import reduce for list reduction

# Lambda function example
sq = lambda x: x ** 2  # Square calculation
print("Square of 5:", sq(5))  # Output: 25

# map() example
nums = [1, 2, 3, 4, 5,9,14,30]  # List of numbers
sqs = list(map(lambda x: x ** 2, nums))  # Squares of numbers
print("Squares using map:", sqs)  # Output: [1, 4, 9, 16, 25, 81, 196, 900]

# filter() example
evns = list(filter(lambda x: x % 2 == 0, nums))  # Even numbers
print("Even numbers using filter:", evns)  # Output: [2, 4, 14, 30]

# reduce() example
sm = reduce(lambda x, y: x + y, nums)  # Sum of numbers
print("Sum using reduce:", sm)  # Output: 68