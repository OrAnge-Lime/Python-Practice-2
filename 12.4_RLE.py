a = input()
n = a[0]
i = 0
while i < a.__len__():
    n = a[i]
    c = 0
    while i < a.__len__():
        if n == a[i]:
            c += 1
            i += 1
        else:
            break
    print(n, c)




