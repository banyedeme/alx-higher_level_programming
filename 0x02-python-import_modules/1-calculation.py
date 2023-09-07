# Import the necessary functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Define variables a and b
a = 10
b = 5

# Perform mathematical operations using the imported functions
sum_result = add(a, b)
difference_result = subtract(a, b)
product_result = multiply(a, b)
quotient_result = divide(a, b)

# Print the results
print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {difference_result}")
print(f"{a} * {b} = {product_result}")
print(f"{a} / {b} = {quotient_result}")
