arr1 = [1,4,2,5,3,9]
arr2 = [5,3,8,9,7,4]
arr =arr1 + arr2
print(arr)
n = len(arr)
temp = set()
for i in range(n):
    temp.add(arr[i])
print(temp)    