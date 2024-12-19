try:
    user_num = int(input('Enter an integer for user_num: '))
    div_num = int(input('Enter an integer for div_num: '))
    result = user_num / div_num
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Quotient:", result)
