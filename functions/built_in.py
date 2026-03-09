import sys
import array
import math
from collections import Counter
from itertools import combinations

# Step 1: Display Python version and executable path using sys module
print("Python Version:", sys.version)
print("Python Executable Path:", sys.executable)

# Step 2: Store numbers in an array
numbers = array.array('i', [5, 10, 15, 10, 5])

# Step 3: Calculate the square of each number using math
squares = [math.pow(num, 2) for num in numbers]

# Step 4: Count occurrences of each number using collections.Counter
number_counts = Counter(numbers)

# Step 5: Generate all pairs of numbers using itertools.combinations
pairs = list(combinations(numbers, 2))

# Step 6: Display results
print("\nNumbers:", list(numbers))
print("Squares:", squares)
print("Number Counts:", number_counts)
print("Pairs:", pairs)