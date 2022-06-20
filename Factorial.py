# i  = 5
# while i >= 0:
#   p = i
#   i = i - 1
#   q = p * i
#   up = q
#   update = up + q
#   print(update, end = " ")

def fact(n):
  f = 1
  for i in range(1, n+1):
    f = f * i
  return f

n = int(input("enter the number you need to get Factorial"))
result = fact(n)


print(result)