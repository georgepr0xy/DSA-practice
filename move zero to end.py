arr = [ 3, 5, 0, 0, 4]
n = len(arr)

# for i in range(n):
#     if arr[i] == 0:

#      for j in range(i,n-1):
#         arr[j]=arr[j+1]
# arr[n-1]=arr[i]
# print(arr)        
temp = []
for i in range(n):
	if arr[i] != 0:
	    temp.append(arr[i])
print(len(arr))		
zero = len(arr)- len(temp)
for j in range(zero):
	temp.append(0)
arr = temp     
print(arr)
#-------------------optimal approach-------------->>

j = -1
for i in range(n):
	if arr[i]==0:
	    j = i
	    break
if j == -1:
	return arr
for i in range(j+1,n):
	if arr[i] != 0:
	    arr[i], arr[j]= arr[j], arr[i]
	    j += 1
  