arr = [1,2,3,4,5]
n = len(arr)
k =2
# temp=[]
# for  i in range(1,len(arr)):
#     temp.append(arr[i])
# temp.append(arr[0])    
# print(temp)

#------------------------>
# x = arr[0]
# for i in range(0,len(arr)-1):
#     arr[i]=arr[i+1]
# arr[-1]=x  
# print(arr)
temp = arr[:k]
for i in  range(0, n-k):
    arr[i] = arr[i+k]
for i in range(n-k,n):
    arr[i]=temp[i] 

print(arr)