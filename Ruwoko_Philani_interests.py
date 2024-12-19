
principal = float(input(" Please enter the principal (original loan amount): $"))
term_in_months = int(input("Please enter the term of the loan in months: "))
annual_interest_rate = float(input("Please enter the annual interest rate (decimal form): "))


monthly_interest_rate = annual_interest_rate / 12
amount_of_interest = principal * (1 + monthly_interest_rate)**term_in_months - principal


print(f"The amount of interest paid on the loan is: ${amount_of_interest:.2f}")
