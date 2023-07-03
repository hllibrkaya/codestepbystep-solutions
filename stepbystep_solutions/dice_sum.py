import random
def dice_sum():
  num=int(input("Desired dice sum: "))
  sum=0
  while(sum!=num):
    a=random.randint(1,6)
    b=random.randint(1,6)
    print(a,"and",b,"=",(a+b))
    sum=a+b