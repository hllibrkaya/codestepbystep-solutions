def word_count (s):
  r=s.split(" ")
  count=0
  for i in r:
    if(i==""):
      count+=1
  for i in range(count):
    r.remove("")
  return len(r)