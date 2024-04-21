arr = [1,2,3,4,5,6,7,8]
n = len(arr)
k=2
temp= arr[n-k:]
print(temp)
for i in range(n-k-1,-1,-1):
    arr[i+k] =  arr[i]
for i in range(k):
    arr[i]=temp[i]
print(arr)