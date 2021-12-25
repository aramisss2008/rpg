list1 = [7, 5, 3, 1, 3, 22, 23, -2, 3]
sum = 0
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        sum += list1[i]
print(sum)