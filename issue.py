def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def print_message(message):
  print(message)  # Missing indentation for the print statement

def add_numbers(a, b):
  result = a + b
  return result

number = 5
factorial_result = factorial(number)
print("Factorial of", number, "is", factorial_result)

print_message("Hello, World!")

result = add_numbers(3, 7)
print("Addition result:", result)

# Missing blank line after function definition
def power(base, exponent):
  return base ** exponent