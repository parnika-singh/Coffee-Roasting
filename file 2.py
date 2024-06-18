def factorial(n):
    if n < 0:
        return "undefined"  # Factorial is not defined for negative numbers
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
n = 5
print(f"The factorial of {n} is {factorial(n)}")  # Output: The factorial of 5 is 120
