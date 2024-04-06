a = int(input("enter the first value:"))
b = int(input("enter the second value:"))
ans = 1
for i in range(1, min(a,b)+1):
    if a%i == 0 and b%i ==0:
        ans = i
print(ans)
