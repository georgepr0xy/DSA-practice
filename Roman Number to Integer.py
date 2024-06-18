a = "VMXDC"
mp = { 'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000

}
ans = 0
for i in range(len(a)):
    if i < len(a) -1 and mp[a[i]] < mp[a[i+1]]:
        ans  -= mp[a[i]]
    else:
        ans += mp[a[i]]    

print(ans)        
