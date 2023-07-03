import random
print("Welcome to Piglet!")
roll=0
point=0
choice="y"
go=True
while (go):
  roll=random.randint(1,5)
  print("You rolled a",roll)
  if(roll == 1):
    point=0
    break
  choice=input("Roll again? ")
  if(choice=="n" or choice=="no"):
    go=False
  point += roll
print("You got",point,"points.")