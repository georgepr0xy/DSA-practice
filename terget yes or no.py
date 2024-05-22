arr = [1, 4, 45, 6, 10, -8]
target = 5
y =0
n = len(arr)
arr.sort()
right = n-1
left = 0
while left < right:
    if arr[left]+arr[right] == target:
       print("yes")
       y =1
       break
       
    elif arr[left]+arr[right] < target:
        left += 1
    else:
        right -= 1
if y == 0:
   print("no")