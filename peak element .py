arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
n = len(arr)
flag = -1
for i in range(n):
    if (i == 0 or arr[i] > arr[i-1]) and (i == n-1 or arr[i] > arr[i+1]):
        flag = i 
print(flag)        