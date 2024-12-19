class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.num + other.num)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.num - other.num)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.num * other.num)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.num != 0:
                # Ensure division by zero is not performed
                return Number(self.num / other.num)
            else:
                print("Error: Division by zero")
                return None
        else:
            return NotImplemented

# Demonstrate the functionality of the Number class
num1 = Number(5)
num2 = Number(3)

# Addition
result_add = num1 + num2
print(f"Addition: {num1} + {num2} = {result_add}")

# Subtraction
result_sub = num1 - num2
print(f"Subtraction: {num1} - {num2} = {result_sub}")

# Multiplication
result_mul = num1 * num2
print(f"Multiplication: {num1} * {num2} = {result_mul}")

# Division
result_div = num1 / num2
print(f"Division: {num1} / {num2} = {result_div}")

# Using all operators
result_combined = num1 + num2 - num2 * num1 / num2
print(f"All operators: {num1} + {num2} - {num2} * {num1} / {num2} = {result_combined}")
