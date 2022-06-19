#Write a program to print the following number pattern using a loop.
row = int(input("Enter the number you need!!"))
for i in range(1, row+1, 1):
   for j in range(1, i+1):
    print(j,end=" ")
   print(" ")
