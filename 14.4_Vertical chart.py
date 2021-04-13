a = input().split(' ')
l = int(max(a)) + 3
w = a.__len__()
list = []
for i in range(l):
    s = ''
    for j in range(w):
        if int(a[j]) >= i:
            s += "*"
        else:
            s += " "
    list.append(s)

v = ''
for i in range(w + 2):
    v += '*'
print(v)

for i in range(list.__len__()-1, 0, -1):
    print('*' + list[i] + '*')
print(v)

