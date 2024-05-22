arr = [2, 3, 5, 1, 9]
n = len(arr)
k = 10
length = 0

# Outer loop to iterate through each element in the array
for i in range(n):
    # Inner loop to iterate through each possible subarray starting from i
    for j in range(i, n):
        s = 0
        # Inner loop to calculate the sum of the subarray from i to j
        for k in range(i, j + 1):
            s += arr[k]
        # If the sum of the subarray is equal to k, update the maximum length
        if s == k:
            length = max(length, j - i + 1)

# Print the length of the longest subarray with sum equal to k
print(length)

#--------------------------------------------------------------------------------------->

