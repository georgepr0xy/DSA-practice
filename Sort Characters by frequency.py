str = "cccaaa"


mp  = {}
answerString =""
for i in range(len(str)):
    if str[i] in mp:
        mp[str[i]] += 1
    else:
        mp[str[i]] = 1
print(mp)
b= sorted(mp.items(), key=lambda x: x[1], reverse= True)
print(b)
for char, frequency in b:
            answerString = answerString + char * frequency
print(answerString)