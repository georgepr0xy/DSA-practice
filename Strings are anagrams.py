s1 = "abcdeabsd"
s2 = "sfasdfasf"
# l1= list(s1)
# l2 = list(s2)
# l1.sort()
# l2.sort()
# print(l1)
# print(l2)
# n =len(l1)
# n = len(l2)
# yes = 0
# for i in range(n):
#     if l1[i]==l2[i]:
#         yes =1
#     if l1[i] != l2[i]:
#         yes = 0
#         break   
# if yes == 1:
#     print("anagram")
#------------------------->
s1 = "ACT"
s2 = "CTA"
l1= list(s1)
l2 = list(s2)
l1.sort()
l2.sort()
if l1 == l2:
    print("anagram")     