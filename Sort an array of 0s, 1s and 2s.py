arr = [2,0,1,0,2,0,2,1]
n = len(arr)
temp= 0
a = 0
b = 0
c = 0
for i in range(n):
    if arr[i]==0:
      a += 1
    if arr[i]==1:
       b += 1
    if arr[i]==2:
       c+=1
arr =[]    
for i in range(a):
    arr.append(0)
for i in range(b):
   arr.append(1)
for i in range(c):
   arr.append(2)   

print(arr)        