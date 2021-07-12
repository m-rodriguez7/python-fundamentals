'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
number = int(input("Enter a number between one and one million: "))

if number % 3 == 0:
    print(f"{number} is divible by 3")
else:
    print(f"{number} is not divisible by 3")