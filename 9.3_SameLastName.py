a = int(input())
names = []
res = 0
for i in range(a):
    names.append(input())
names2 = set(names)
for i in names2:
    if names.count(i) > 1:
        res += names.count(i)
print(res)
