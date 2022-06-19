#Write a program to print multiplication table of a given number
print("Print multiplication table of a given number")
#initilize the variables
data = int(input())
limit = 10
i = 0
#itteration statment starts
while  i <= limit:
  z = i * data
  if  z > 0:
    print(z)
  i = i + 1