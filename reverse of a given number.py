#Reverse a given integer number
n = int(input("value: "))
rev = 0
while n > 0:
  rev = (rev * 10) + n % 10
  n = n // 10
print("Reversed value= ", rev)
