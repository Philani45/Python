class NegativeValueError(Exception):
    pass

def steps_to_miles(steps):
    try:
        # Attempt to convert the input to an integer
        steps = int(steps)

        # Check if the number of steps is negative
        if steps < 0:
            raise NegativeValueError("Exception: Negative Step Count Entered.")

        # Convert steps to miles (1 mile for every 2000 steps)
        miles = steps / 2000
        return miles

    except ValueError:
        # Handle non-numeric input
        raise ValueError("Exception: Non-Numeric Value Entered.")

# Program to read the number of steps from the user and call steps_to_miles()
try:
    user_input = input("Enter the number of steps: ")
    result = steps_to_miles(user_input)
    print(f'Miles walked: {result:.2f}')

except (ValueError, NegativeValueError) as e:
    # Catch and handle exceptions
    print(e)
