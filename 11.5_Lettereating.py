a = input()
while a.__len__() > 1:
    print(a)
    a2 = ''
    for i in range(1, a.__len__()-1):
        a2 += a[i]
    a = a2

