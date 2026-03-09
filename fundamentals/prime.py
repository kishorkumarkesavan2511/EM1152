# Get the upper limit 'n' from the user
n = int(input("Enter the number up to which you want to generate prime numbers: "))
# num = 19
# Loop through numbers from 2 to 'n' (since 1 is not a prime number)
for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # If 'num' is divisible, it's not a prime number
                print(num,"is not prime", end=" ")
                break  # Exit the inner loop if 'num' is not prime
            else:
                continue  # Continue the inner loop if 'num' is not divisible by 'i'
    else:
            # If the inner loop is not broken, 'num' is a prime number
                print(num,"is prime", end=" ")

      