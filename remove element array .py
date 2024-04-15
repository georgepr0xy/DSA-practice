arr = [2,3,2,4,6,3,2,7,9]
k =set()
for i in arr:
    k.add(arr)
print(k)   
#---------------------------optimal approach------->

i = 0
for j in range(1,len(arr)):
    if arr[j] != arr[i]:
        