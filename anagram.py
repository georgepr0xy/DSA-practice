string1 = input("enter the string 1")
string2 = input("enter the string 2")
if (len(string1) != len(string2)):
    print("this is not a string")
else:
    string1 = sorted(string1)
    string2 = sorted(string2)
if string1==string2:
    print("this is anagram")
else: print("this is not anagram")     