'''
Print out every prime number between 1 and 100.

'''
for i in range(1,100):
    for j in range(2,(i+1)):
        if i%j==0:
            if i==j:
                print(i)
            break