from pip import main
def fibnum(n):
  pn = 0 
  cn = 1
  i = 0
  while i <= n:
    for i in range(0, n):
      #Updation of values
      ppn = pn
      pn = cn
      cn = ppn + pn 
      print(cn)
    return cn
    
  i+=1

if __name__=="__main__":
  num = int(input("value: "))
  result =  fibnum(num)


