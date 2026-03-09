# Get the input string from the user
s = input("Enter a string: ")

# Create an empty dictionary to store the frequency of characters
freq = {}

# Iterate through each character in the string
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# Print the frequency of characters in horizontal format
print("Frequency of characters in the string: ", end="")
for c in freq:
    print(f"{c}: {freq[c]}", end=" ")