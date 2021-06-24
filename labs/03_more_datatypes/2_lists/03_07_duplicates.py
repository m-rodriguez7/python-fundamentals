'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5, 2, 2, 2, 6]

new_list = []

for x in list_:
    if x not in new_list:
        new_list.append(x)

print(f'Original list: {list_}')
print(f'List after removing duplicates: {new_list}')
