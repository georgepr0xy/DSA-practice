s = "504"
# n= len(s)
# print(n)
# l = []
# for i in s:
#     l.append(int(i))
# print(l)
# if l[n-1] % 2 != 0:
#     print(s)
# else:    
#    l.sort(reverse= True)
#    print(l)
#    s =[]
#    for i in l:
#        if i % 2 != 0:
#            s.append(str(i))
#            break
#    print(''.join(s))

# #-------------------------------------------->
for i in range(len(s)-1,-1,-1):
    if int(s[i]) % 2 != 0:
        print(s[:i+1])
    else: print("")            
