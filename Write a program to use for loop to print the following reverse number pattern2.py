# Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
#initilize the variables
n = 5
k = 5
#itteration statment starts
for i in range(0, n+1):
    for j in range(k-i , 0 , -1):
        print(j, end=' ')
    print()