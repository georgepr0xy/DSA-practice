import sys
arr = [1,2 ,3, -2, 5]
n = len(arr)
# maxi = -sys.maxsize-1
# for i in range(n):
    
#     for j in range(n):
#         sum = 0
#         for k in range(i,j+1):
#             sum = sum +arr[k]
#             maxi = max(maxi,sum)
# print(maxi)    

# maxi = -sys.maxsize-1
# for i in range(n):
#     sum = 0
#     for j in range(i,n):
#       sum += arr[j]
#       maxi = max(maxi , sum)
# print(maxi)
maxi = -sys.maxsize -1
sum = 0
for i in range(n):
    sum = sum + arr[i]
    if sum > maxi:
        maxi = sum
    if sum < 0:
        sum = 0
print(maxi)