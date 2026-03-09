# Fixed size of matrices
n = 2  # 2x2 matrices

# Define the first and second matrices
a = [[1, 2], [3, 4]]  # First matrix
b = [[5, 6], [7, 8]]  # Second matrix

# Initialize result matrices with zeros
add = [[0, 0], [0, 0]]  # Result matrix for addition
sub = [[0, 0], [0, 0]]  # Result matrix for subtraction
mul = [[0, 0], [0, 0]]  # Result matrix for multiplication

# Perform matrix addition and subtraction
for i in range(n):
    for j in range(n):
        add[i][j] = a[i][j] + b[i][j]
        sub[i][j] = b[i][j] - a[i][j]

# Perform matrix multiplication
for i in range(n):  # Loop over rows of the first matrix
    for j in range(n):  # Loop over columns of the second matrix
        for k in range(n):  # Loop over elements in rows and columns
            mul[i][j] += a[i][k] * b[k][j]




# Display result matrices
print("Resultant Matrix after Addition:")
for row in add:
    print(row)

print("Resultant Matrix after Subtraction:")
for row in sub:
    print(row)

print("Resultant Matrix after Multiplication:")
for row in mul:
    print(row)
