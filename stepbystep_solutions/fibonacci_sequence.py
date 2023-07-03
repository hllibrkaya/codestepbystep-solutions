num=int(input("This program lists the Fibonacci sequence.\nMax value? "))
arr=[0,1]
i=1
res=""
if(num==0):
  print(0)
else:
  while (not(arr[len(arr)-1]>num)):
    arr.append(arr[i]+arr[i-1])
    i += 1
for i in arr[0:len(arr)-1]:
  res +=(str(i) + ", ")
print(res[0:len(res)-2])








