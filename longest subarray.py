arr =[2,3,5,1,9]
n = len(arr)
k = 5
for i in range(0,n):
    for j in range(i,n):
        s = 0
        for k in range(i,j+1):
            s += arr[i]
        if s == k:
           print(len())