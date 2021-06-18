'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
string = input("Enter a string: ").lower()
vowels = 'aeiou'

count = 0
for char in string:
    if(char in vowels):
        count = count + 1

print(f'Number of vowels in string: {count}')

dic = {}.fromkeys(vowels,0)
for char in string:
    if(char in vowels):
        dic[char] += 1

for i in dic:
    print(f'{i} => {dic[i]}')







