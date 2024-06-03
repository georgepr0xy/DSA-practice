s= "this is an amazing program"
# li =[]
# newli =[]
# li=s.split(" ")
# n =len(li)
# print(li)
# for i in range(n-1,-1,-1):
#     newli.append(li[i])
# for j in range(n):
#     print(newli[j],end=' ')   

#-----------> using stack ------------->
# words= s.split()
# print(words)
stack =s.split()
# for word in stack:
#     stack.append(word)
    
reversed_string =""     
while stack:
    reversed_string += stack.pop()
    if stack:
        reversed_string += " "
print(reversed_string)
