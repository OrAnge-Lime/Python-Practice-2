a = input()
d = dict()
for i in range(a.__len__()):
    if d.__contains__(a[i]):
        d[a[i]] += 1
    else:
        d[a[i]] = 1

s = 0
for i in d:
    if d[i] > s:
        s = d[i]

print(s)

