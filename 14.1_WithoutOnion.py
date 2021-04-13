n = int(input())
list = []
for i in range(n):
    a = input()
    if not a.__contains__('лук'):
        list.append(a)

res = ''
for i in range(list.__len__()):
    if i != list.__len__():
        res += list[i] + ", "
    else:
        res += list[i]
print(res)