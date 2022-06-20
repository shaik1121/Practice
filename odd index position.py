# Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# we are starting an index with one then we are using "::" for steping and we are steping 2.
for i in my_list[1::2]:
  print(i, end=" ")
        