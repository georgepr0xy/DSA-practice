arr =[1,2,-4,-5]
# pos=[]
# neg=[]
n = len(arr)
# for i in range(n):
#     if arr[i] > 0:
#         pos.append(arr[i])
#     else :
#         neg.append(arr[i])

# for i in range(len(pos)):
#     arr[2*i] = pos[i]
# for i in range(len(neg)):
#     arr[2*i +1]= neg[i] 
# print(arr)    


#------------------------------=optimal-------------------->
posindex =0
negindex = 1
a =[0]*n 
for i in range(n):
    if arr[i] > 0:
        a[posindex] = arr[i]
        posindex += 2    
    else:
        a[negindex] = arr[i]
        negindex += 2
print(a)        