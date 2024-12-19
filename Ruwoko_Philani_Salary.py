# Gather information from the user
wage = float(input("Please enter your hourly wage: $"))
hours_per_week = float(input(" Please enter the number of hours worked per week: "))
weeks_per_year = int(input("Please enter the number of weeks worked this year: "))


annual_salary = wage * hours_per_week * weeks_per_year


print(f"Your annual salary is: ${annual_salary:.2f}")
