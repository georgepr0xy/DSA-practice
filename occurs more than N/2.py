from collections import Counter
arr = [4,4,2,4,3,4,4,3,2,4]
n = len(arr)
count = 0
y = 0
for i in range(n):
    count = 0
    for j in range(i,n):
        if arr[i]== arr[j]:
            count += 1
    if count > n//2:
           print(arr[i])

#---------------------------------------
counter  = Counter(arr)
print(counter)
for num, count in counter.items():
     if count > n//2:
         print(num)