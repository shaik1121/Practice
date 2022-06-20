#Use else block to display a message “Done” after successful execution of for loop
i = 0
n=5
while i <= n:
  if i < n:
    for i in range(n):
      print(i)
      i = i + 1
  else:
    print("Done")
    i = i + 1