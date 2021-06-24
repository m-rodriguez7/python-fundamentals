'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
string = input("Enter string: ")

result_list = []

for x in string.split():
    result_list.append(tuple(x))

print(result_list)