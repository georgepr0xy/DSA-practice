a = [3, 4, 6, 7, 9, 12, 16, 17]
n = len(a)
target =  6
low = 0
high = n-1
while low <= high :
    mid = (low + high) // 2
    if a[mid] == target:
        print(mid)
    if target > a[mid]:
        low = mid + 1
    else: 
        high = mid -1 
            