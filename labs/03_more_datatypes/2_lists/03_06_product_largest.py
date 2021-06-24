'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
num_list = []
print("Enter 10 intergers")
for num in range(10):
    num_list.append(int(input("Enter number: ")))

print(num_list)
print(f'Max number is: {max(num_list)}')

product = 1
for num in num_list:
    product = product * num

print(f'The product of all the number is: {product}')

