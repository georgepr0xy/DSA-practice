s = "(()())(())"
result = []
balance = 0 
for i in s:
    if i == '(':
        if balance > 0:
            result.append(i)
        balance += 1
    
    elif i == ')':
        balance -= 1
        if balance > 0:
            result.append(i)

print(''.join(result))