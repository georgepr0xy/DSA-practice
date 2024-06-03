arr =[3, 1, 2, 4]
target = 6
n = len(arr)
count =0
for i in range(n):
    
    for j in range(i,n):
        sumarr = sum(arr[i:j+1])
        if sumarr == target:
            count += 1

print(count)