def print_palindrome():
  s1=input("Type one or more words: ")
  s=s1.lower()
  isPal=False
  if(len(s)%2==0):
    for i in range(int(len(s)/2)):
      if(s[i]==s[len(s)-1-i]):
        isPal=True
      else:
        isPal=False
        break
  else:
    for i in range(int(((len(s)-1)/2)-1)):
      if(s[i]==s[len(s)-1-i]):
        isPal=True
      else:
        isPal=False
        break
  if(isPal):
    print(s1,"is a palindrome!")
  else:
    print(s1,"is not a palindrome.")