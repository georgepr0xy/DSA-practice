arr = [1,2,3,4,5,6,7]
n= len(arr)
k = 2
temp = arr[:k]
print(temp)
for i in  range(0, n-k):
    arr[i] = arr[i+k]
for i in range(0,k):
    arr[n-k+i] = temp[i]
    print(arr)