num = int(input())
p = []
for i in range(num):
    p.append(input() + " " + input())

for i in range(-1, p.__len__() * (-1), -1):
    print(p[i])

