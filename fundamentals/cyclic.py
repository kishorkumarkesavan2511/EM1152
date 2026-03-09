# Input number limit
n = int(input("Enter the limit: "))

for x in range(2, n + 1):
    if all(x % d != 0 for d in range(2, int(x ** 0.5) + 1)):    # Check if x is a prime number
        s, cp = str(x), True  # Convert to string and assume cyclic prime
        for j in range(len(s)):
            r = int(s[j:] + s[:j])  # Generate rotation
            if any(r % d == 0 for d in range(2, int(r ** 0.5) + 1)):  # Check if not prime
                cp = False
                break
        if cp:
            print(x, end=" ")