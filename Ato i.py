s= " "
num = '0123456789'
res = ''
for x in s:
    if x == ' ' and len(res) == 0:
        continue
    if x != ' ' and (x in '-+' or x in num) and len(res) == 0:
        res += x
    elif x in num:
        res += x
    else:
        break
if res == '' or res in '-+':
    print(0)
else:
    if int(res) < -(2**31):
      print(-(2**31))
    elif int(res) > (2**31 - 1):
          print(2**31 - 1)
    else:
        print(int(res))