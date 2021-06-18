'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
investment_amount = float(input("Enter investment amount: "))
interest_rate = float(input("Enter interest rate in percentage: "))
years = int(input("Enter numbers of years to invest: "))

future_value = investment_amount * (1 + (interest_rate/100)) ** years

print(future_value)