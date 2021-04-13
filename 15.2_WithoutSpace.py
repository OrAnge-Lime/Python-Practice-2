a = input().split(" ")
s = 0
for i in range(a.__len__()):
    s += a[i].__len__()
print(s)