n = int(input())
l = []
for i in range(n):
    l.append(input())
k = int(input())

res = []
while l.__len__() > 0:
    i = 0
    while i < l.__len__():
        res.append(l[i])
        l.remove(l[i])
        i += k - 1

print(res)
