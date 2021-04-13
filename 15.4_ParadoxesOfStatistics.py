import math

n = int(input())
l = []
for i in range(n):
    a = input().split(" ")
    result = [int(item) for item in a]
    l.append(result)


# медиана каждого набора,
s1 = []
for i in range(l.__len__()):
    l[i].sort()
    s1.append(l[i][math.ceil(l[i].__len__()/2)])
print(s1)

# мода каждого набора,
s2 = []
for i in range(l.__len__()):
    d = dict()
    for j in l[i]:
        if j in d:
            d[j] += 1
        else:
            d[j] = 0

    maxv = 0
    num = l[0]
    for j in d:
        if d[j] > maxv:
            num = j
            maxv = d[j]
    s2.append(num)
print(s2)

# медиана медиан,
s1.sort()
print(s1[math.ceil(s1.__len__()/2)-1])

# мода мод,
d2 = dict()
for j in s2:
    if j in d2:
        d2[j] += 1
    else:
        d2[j] = 0

maxv = 0
num = s2[0]
for j in d2:
    if d2[j] > maxv:
        num = j
        maxv = d2[j]
mm = num
print(mm)

# медиана чисел из всех наборов, взятых вместе,
suml = []
for k in l:
    for p in k:
        suml.append(p)


suml.sort()
res = suml[math.ceil(suml.__len__()/2)]
print(res)

# мода чисел из всех наборов, взятых вместе.
d3 = dict()
for j in suml:
    if j in d3:
        d3[j] += 1
    else:
        d3[j] = 0

maxv = 0
num = suml[0]
for j in d3:
    if d3[j] > maxv:
        num = j
        maxv = d3[j]
mm = num
print(mm)
