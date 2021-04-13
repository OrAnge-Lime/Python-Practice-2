n = int(input())
m = []
for i in range(n):
    a = input()
    if a[0] != "#" or a[1] != "#" or a[2] != "#" or a[3] != "#":
        if a[0] == "%" and a[1] == "%%":
            m.append(a.replace("%%", ""))
        else:
            m.append(a)
print(m)
