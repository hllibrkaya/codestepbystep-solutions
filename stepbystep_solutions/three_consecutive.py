def three_consecutive(a,b,c):
  l=[a,b,c]
  l.sort()
  if( (l[0]+1)==l[1] and (l[1]+1)==l[2] ):
    return True
  else:
    return False