arr = [4,1,2,1,2,4,5]
n = len(arr)
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if arr[i] == arr[j]:
#             count += 1
#     if count < 2:
#         print(arr[i])        
#---------------------------optimal------------>


xorr = 0
for i in arr:
    xorr ^= i
print(xorr)    