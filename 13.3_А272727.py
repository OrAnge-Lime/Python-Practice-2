a = int(input())
n = [0]
m = [0]
for i in range(a - 1):
    next = 0
    for j in range(n.__len__()):
        if n[j] == m[j]:
            next += 1
    n.append(next)
    m.insert(0, next)
print(n)
