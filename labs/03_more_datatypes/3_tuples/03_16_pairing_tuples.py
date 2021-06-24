'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

num_list = [10,2,3,4,5,6,7,8,9,1,11]
num_list.sort()

new_list = []

for x in range(0,len(num_list),2):
    try:
        new_list.append((num_list[x],num_list[x+1]))
    except:
        new_list.append((num_list[x],0))

for i in new_list:
    print(i)
