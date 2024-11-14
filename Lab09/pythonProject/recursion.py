# Task 1: Calculate the product of the digits of an integer
def product_of_digits(x):
    x = abs(x)  # Ensure x is positive
    if x < 10:  # Base case: single digit
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)

# Task 2: Convert a list of integers to a comma-separated string
def array_to_string(a, index=0):
    if index == len(a) - 1:  # Base case: last element
        return str(a[index])
    else:
        return str(a[index]) + ',' + array_to_string(a, index + 1)

# Task 3: Recursive logarithm calculation
def log(base, value):
    if value <= 0 or base <= 1:
        raise ValueError("Base must be greater than 1, and value must be greater than 0")
    if value < base:  # Base case: value less than base
        return 0
    else:
        return 1 + log(base, value // base)

# Test code
if __name__ == "__main__":
    # Test Task 1 - Various cases for product_of_digits
    print("Task 1: product_of_digits(234) =", product_of_digits(234))  # Expected output: 24
    print("Task 1: product_of_digits(12) =", product_of_digits(12))    # Expected output: 2
    print("Task 1: product_of_digits(-12) =", product_of_digits(-12))  # Expected output: 2

    # Test Task 2: array_to_string
    print("Task 2: array_to_string([1, 2, 3, 4]) =", array_to_string([1, 2, 3, 4]))  # Expected output: "1,2,3,4"
    print("Task 2: array_to_string([10, 20, 30]) =", array_to_string([10, 20, 30]))  # Expected output: "10,20,30"

    # Test Task 3: log - using examples provided in Lab 09
    print("Task 3: Example 1: int(log10(123456)) =", log(10, 123456))  # Expected output: 5
    print("Task 3: Example 2: int(log2(64)) =", log(2, 64))            # Expected output: 6
    print("Task 3: Example 3: int(log10(4567)) =", log(10, 4567))      # Expected output: 3
