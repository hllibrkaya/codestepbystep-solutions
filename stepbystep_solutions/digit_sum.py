def digit_sum(num):
  if(num<0):
    num=num*(-1)
  num=str(num)
  new=0
  for i in num:
    new += int(i)
  return new