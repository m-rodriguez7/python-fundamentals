'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(num_list):

    sum = 0
    for n in num_list:
      sum += n

    max_num = max(num_list)
    print(f"Max Number: {max_num}")

    min_num = min(num_list)
    print(f"Min Number: {min_num}")

    average = float(sum / len(num_list))
    print(f"Average: {average}")

    print(f"Sum: {sum}")

# call the function below here
print(example_list)
stats(example_list)
