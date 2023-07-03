def second_half_letters(s):
  s=s.lower()
  counter=0
  for i in s:
    if(ord(i)>ord("m")):
      counter +=1
  return counter