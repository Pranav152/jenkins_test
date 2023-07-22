def factorial(num_1):
    if num_1 == 0:
        return 1
    else:
        return num_1 * factorial(num_1-1)

def print_message(message):
    print(message)  # Fix the missing indentation for the print statement

def add_numbers(num_1, num_2):
    result = num_1 + num_2
    return result

NUMBER = 5
factorial_result = factorial(NUMBER)
print("Factorial of", NUMBER, "is", factorial_result)

print_message("Hello, World!")

RESULT = add_numbers(3, 7)
print("Addition RESULT:", RESULT)

# Add a blank line after function definition
def power(base, exponent):
    return base ** exponent
