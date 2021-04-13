c = int(input())
d = dict()

for i in range(c):
    inp = input()
    d[inp.split(" ")[0] + " " + inp.split(" ")[1]] = inp.split(" ")[-1]

a = int(input())
l = []
for i in range(a):
    l.append(input())

for i in range(l.__len__()):
    s = ""
    for j in d:
        if d[j] == l[i]:
            s += j + " "
    print(s)
