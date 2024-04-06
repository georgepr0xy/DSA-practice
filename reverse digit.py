digit = int(input("Enter the digit"))
temp = digit
reverse = 0
while temp>0:
     remainder = digit % 10 
     reverse = (reverse*10)+ remainder
     temp= temp//10
     print(reverse)
