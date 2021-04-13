n = int(input())
m = int(input())
list = []
for i in range(n):
    list.append(input())

for i in range(0, n, 2):
    s = ''
    for j in range(0, m, 2):
        s += list[i][j]
    print(s)