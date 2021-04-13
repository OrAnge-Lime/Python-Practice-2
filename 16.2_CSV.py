def m(s):
    l = s.split(",")
    i = 0
    while i < l.__len__():
        if l[i].startswith('"'):
            while not l[i].endswith('"') or i >= l.__len__():
                l[i] = "".join([l[i], l[i + 1]])
                l.remove(l[i + 1])
                i += 1
        i += 1
    return l


a = int(input())
l = []
for i in range(a):
    l.append(m(input()))

b = int(input())
loutput = []
for i in range(b):
    loutput.append(input().split(","))

for i in range(b):
    print(l[int(loutput[i][0])][int(loutput[i][1])])



