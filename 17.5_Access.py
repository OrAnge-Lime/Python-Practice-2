a = int(input())
access = []
for i in range(a):
    access.append(input())

b = int(input())
paths = []
for i in range(b):
    b = input()
    n = "NO"
    for j in access:
        if b.startswith(j):
            n = "YES"
    paths.append(n)

print(paths)
