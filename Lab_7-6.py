"""
Create a Python file named lab_7-6.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a 2 separate functions within the same document. 
Create a 3rd function which requires both the first two functions within it
Create 4 test cases for your 3rd function. 
"""
# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Function that requires the first two functions
def combine_operations(x, y, z):
    # Using the first function
    result_add = add_numbers(x, y)
    
    # Using the second function
    result_multiply = multiply_numbers(result_add, z)
    
    return result_multiply

# Test cases for the combine_operations function
test_case_1 = combine_operations(2, 3, 4)
print("Test Case 1:", test_case_1)  # Expected output: (2 + 3) * 4 = 20

test_case_2 = combine_operations(0, 5, 2)
print("Test Case 2:", test_case_2)  # Expected output: (0 + 5) * 2 = 10

test_case_3 = combine_operations(-1, 2, 3)
print("Test Case 3:", test_case_3)  # Expected output: (-1 + 2) * 3 = 3

test_case_4 = combine_operations(10, 0, 1)
print("Test Case 4:", test_case_4)  # Expected output: (10 + 0) * 1 = 10
