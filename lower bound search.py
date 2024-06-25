arr = [3, 5, 8, 15, 19]
n = 5
x = 4
low = 0
high  = n-1
floor_index = -1
while low <= high:
    mid = (low+high)//2
    if x == arr[mid]:
        print(mid)
        
    if x > arr[mid]:
        floor_index = mid
        low = mid + 1
    else :
        high = mid - 1
print(floor_index)         