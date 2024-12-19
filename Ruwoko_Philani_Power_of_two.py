def is_power_of_two(n):
    # Base case: if n is 1, it is a power of two
    if n == 1:
        return True
    # Base case: if n is less than 1 or not divisible by 2, it is not a power of two
    elif n < 1 or n % 2 != 0:
        return False
    # Recursively check if n/2 is a power of two
    else:
        return is_power_of_two(n // 2)

# Get input from the user
try:
    n = int(input("Enter an integer: "))
    result = is_power_of_two(n)
    print(f"{n} is a power of two: {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
