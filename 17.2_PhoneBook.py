a = int(input())
d = dict()
for i in range(a):
    str = input().split(" ")
    d[str[0]] = str[1]

b = int(input())
l = []
for i in range(b):
    l.append(input())

for i in range(l.__len__()):
    res = ''
    for j in d:
        if d[j] == l[i]:
            res += j + " "
    if res == "":
        print("Нет в телефонной книге")
    else:
        print(res)

