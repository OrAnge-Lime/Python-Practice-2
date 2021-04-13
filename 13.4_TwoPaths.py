s = int(input())
start1 = []
start2 = []
for i in range(s):
    k = int(input())
    start1.append(k)
    start2.append(k)

t = int(input())
for i in range(t):
    b = int(input())
    index = int(input())
    r = int(input())
    if b == 1:
        start1[index] += r
    elif b == 2:
        start2[index] += r
    else:
        print("ERROR")
        break

cov = 0
for i in range(s):
    if start1[i] == start2[i]:
        cov += 1

print(start1)
print(start2)
print(cov)