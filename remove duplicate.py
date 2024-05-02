arr = [1,1,2,2,2,3,4,4,5]
n = len(arr)
i = 0
for j in range(1,n):
    if arr[i] != arr[j]:
         i += 1
         arr[i]=arr[j]
print(i+1)