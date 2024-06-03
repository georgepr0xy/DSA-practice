arr = [[1,2,3],[4,5,6],[7,8,9]]

n = len(arr)
# rotated =[[0 for _ in range(n)] for _ in range(n)]
# print(rotated)
# for i in range(n):
#     for j in range(n):
#        rotated[j][n-i-1] = arr[i][j]
# print(rotated)      

#-----------optimal--------------->
for i in range(n):
    for j in range(i):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)        