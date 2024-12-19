def recursive_digit_sum(n):
    # Base case: if n is a single-digit number, return n
    if n < 10:
        return n
    # Recursive case: calculate the sum of digits for n/10 and add the last digit (n % 10)
    else:
        return recursive_digit_sum(n // 10) + (n % 10)

# Get input from the user
try:
    n = int(input("Enter a positive integer: "))
    
    if n < 0:
        print("Please enter a positive integer.")
    else:
        result = recursive_digit_sum(n)
        print(f"Sum of the digits of {n}: {result}")

except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
