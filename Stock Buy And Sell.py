prices = [7,6,4,3,1]
n = len(prices)
maxpro =0

for i in range(n):
    for j in range(i+1,n):
        if prices[i] < prices[j]:
            diff = prices[j]- prices[i]
            maxpro = max(diff,maxpro)
print(maxpro)            