n0 = int(input())
n = []
res = []
for i in range(n0):
    n.append(input())

k = int(input()) # количество перестановок
for i in range(k):
    num = int(input())
    for j in range(num):
        p = int(input()) - 1
        res.append(n[p])
    n.clear()
    n = res.copy()
    res.clear()

print(n)