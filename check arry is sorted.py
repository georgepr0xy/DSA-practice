arr = [1,2,6,4,5]
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        print("array is sorted ")
    else:
        print("the array is not sorted")    
#---------------------------------------