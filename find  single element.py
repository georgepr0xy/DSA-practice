arr = [4,1,2,1,2]
n = len(arr)
count = 0
for i in range(n):
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    if count < 2:
        print(arr[i])        