# arr = [1,2,3,5]
# n = len(arr)
# for i in range(n):
#     if arr[i] != i+1:
#         print(i+1)
#         break


arr = [1,3,5,4,2,7,9,6]
n= len(arr)+1
summarization = (n*(n+1)//2)
s2 = sum(arr)
missing  = summarization-s2
print("the missing number is : ", missing)
