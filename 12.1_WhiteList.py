n1 = int(input())
n = []
for i in range(n1):
    n.append(input())

m1 = int(input())
m =[]
for i in range(m1):
    a = input()
    if n.__contains__(a):
        m.append(a)

print(m)

