'''
Write a script that takes in a number from the user as input and prints the following structure.

Suppose the input is 5, you will output
*
* *
* * * 
* * * *
* * * * * 
i.e. number of rows will be 5, 1st row will have 1 star, 2nd row will have 2 stars, 3rd row 3 stars, 4th row will have 4 stars and 5th row will have 5 stars.

Another example: if input is 3, you will output
*
* *
* * *

Hint: Think of nested for loops

'''
n = 10

for i in range(n+1):
    for k in range(i):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(i+1):
        print("*", end="")
    for k in range(1,i+1):
        print("", end="*")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*", end=" ")
    print()