'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
a = float(5)
print(a)

#converting a float to an interger loses the decimal value
b = int(5.2)
print(b)

#floor devision loses the decimal value
c = 5.2//2
print(c)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The result is " + str(num1 * num2))

