arr = [10, 22, 12, 3, 0, 6]
n = len(arr)
# leader = arr[n-1]
# a = []
# b= []
# a.append(arr[n-1])
# for i in range(n,-1,-1):
#     if leader < arr[i-1]:
#         leader = arr[i-1]
#         a.append(leader)
# print(a) 
# n= len(a)-1       
# for j in range(n,-1,-1):
#     b.append(a[j])
# print(b)

#---------------------another sol ---------->

ans= []
for i in range(n):
    leader = True
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            leader = False
            break
    
    if leader:
        ans.append(arr[i])
print(ans)        