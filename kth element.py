arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
new_arr = arr1 + arr2 
print(new_arr)
n = len(arr1)
m = len(arr2)
print(n)
print(m)

k = 5
n = n+m
print(n)
for i in range(n-1,0,-1):
    for j in range(0,i):
        temp = new_arr[j]
        if new_arr[j] > new_arr[j+1]:
            new_arr[j] = new_arr[j+1]
            new_arr[j+1] = temp
print(new_arr)            
print(new_arr[k])