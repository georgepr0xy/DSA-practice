array = [0,1, 1, 0, 1,1,1,1,1, 1,0,1,1,1,1,1]
n = len(array)
count = 0
max_count = 0
for i in range(n):
    if array[i] == 1:
        count += 1
        if count > max_count:
            max_count= count
    if array[i] == 0:
        count = 0
print(max_count)           