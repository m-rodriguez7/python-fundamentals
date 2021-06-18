'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
string3 = input("Enter third string: ")

print(f'The lenght of {string1} is {len(string1)}')
print(f'The lenght of {string2} is {len(string2)}')
print(f'The lenght of {string3} is {len(string3)}')