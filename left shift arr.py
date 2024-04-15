arr = [1,2,3,4,5]
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
for i in range(len(arr)-1,0,-1):
    print(arr[i])

