def matrix_add(a,b):
   new=[]
   new2=[]
   for i in range(len(b)):
       for j in range(len(a[0])):
               c = a[i][j] + b[i][j]
               new.append(c)

       new2.append(new[0:len(a[0])])
       new.clear()
   return new2