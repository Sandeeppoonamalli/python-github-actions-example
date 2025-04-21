# sum.py

# Addition function
def add_numbers(a, b):
    return a + b

# Subtraction function
def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
    num1 = 5
    num2 = 10
    sum_result = add_numbers(num1, num2)
    diff_result = subtract_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}.")
    print(f"The difference between {num1} and {num2} is {diff_result}.")
