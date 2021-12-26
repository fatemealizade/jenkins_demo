li = [1, 2, 3, 4]
li_to_add = [4, 3, 2, 1]

for i in range(len(li)):
    li_to_add[i-1] = li_to_add[i-1] + li[i-1]

print(li_to_add)