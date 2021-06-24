'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
string = input("Enter a string: ")

word_list = string.split()

print(f'The word with most occurances is {max(word_list,key=word_list.count)}')