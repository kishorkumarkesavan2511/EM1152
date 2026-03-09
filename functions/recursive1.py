def ch(st):
    # Base case: If the string is empty, return 0
    print(f"Processing string: '{st}'")  # Debug statement to show the current string being processed
    if st == "":
        return 0
    # Recursive case: Count the first character and recurse for the rest of the string
    return 1 + ch(st[1:])

# Get input from the user
ist = input("Enter a string: ")
print("The number of characters in the string is:", ch(ist))