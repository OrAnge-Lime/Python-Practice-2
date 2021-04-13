def pr(s, n):
    x = 0
    p = ''
    if n != 0:  # подсчет количества пробелов в начале строки
        while s[x] == " ":
            x += 1
            p += " "

    s2 = ""  # создание новой строки
    for i in range(x, s.__len__()):
        s2 += s[i]

    ss = s2.split(" ")
    sss = []
    for i in ss:
        if i != "":
            sss.append(i)
    s = p +  " ".join(sss)

    return s


def slesh(s):
    m = s.split("'")
    i = 0
    while i < m.__len__():
        if m[i].endswith("\\") and not m[i].endswith("\\\\"):
            m[i] += "'"
            m[i] = ''.join([m[i], m[i + 1]])
            m.remove(m[i + 1])
        i += 1

    t = True
    res = []
    for i in range(m.__len__()):
        if i % 2 == 0:
            if not m[i].__contains__("#"):
                if i == 0:
                    m[i] = pr(m[i], 1)
                else:
                    m[i] = pr(m[i], 0)
            else:
                if i == 0:
                    m[i] = pr(m[i].split("#")[0], 1)
                else:
                    m[i] =pr(m[i].split("#")[0], 0)
                res.append(m[i])
                break
        else:
            m[i] = "'" + m[i] + "'"

        res.append(m[i])

    return "".join(res)


a = int(input())
l = []
for i in range(a):
    l.append(slesh(input()))

for i in range(a):
    print(l[i])
b = input()
print(pr(b, 1))
