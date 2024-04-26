arr = [8,9,10,4,2,8,3,4,9]
# arr.sort()
# print(arr[-2])
# small = float('inf')
# second_small = float('inf')
# large = float('-inf')
# print(large)

# better approach

n = len(arr)
largest = 0 
smallest = arr[0]
for i in range(n):
    if arr[i] >= largest:
        largest = arr[i]
for j in range(n):
     if arr[j] <= smallest:
         smallest = arr[j]
second_largest =float("-inf")       
second_small = float('inf')
for j in range(n):
    if arr[j] > smallest and arr[j] <= second_small:
        second_small = arr[j]
    if arr[j] < largest and arr[j] > second_largest:
        second_largest = arr[j]    
print(second_small)  
print(second_largest)     
#-------------------------------------------->

class Solution:
	def print2largest(self,arr, n):
	    if n < 2:
	     return -1
	    else:
		    large = float("-inf")
            for i in range(n):
              large = max(large, arr[i])
            second_large = float("-inf")
            
            for j in range(n):
                if arr[j] < large and arr[j] > second_large:
                    second_large = arr[j]
            if second_large == float("-inf"):
                  return -1
            return second_large  
                  
            