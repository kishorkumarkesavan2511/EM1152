import sys

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)
diff = num1 - num2
print("The difference when", num2, "is subtracted from", num1, "is:", diff)
prod = num1 * num2
print("The product of", num1, "and", num2, "is:", prod)
quot = num1 / num2
print("The quotient of", num1, "and", num2, "is:", quot)
div = num1 // num2
print("The floor division of", num1, "by", num2, "is:", div)
mod = num1 % num2
print("The modulus of", num1, "and", num2, "is:", mod)
exp = num1 ** num2
print("The result of", num1, "raised to the power of", num2, "is:", exp)