def print_factors(num):
  s=""
  for i in range(1,num+1):
    if(num%i==0):
      s += str(i)+" and "
  print(s[0:len(s)-5])