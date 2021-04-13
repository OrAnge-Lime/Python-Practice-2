def code(l, p, a):
    i = 0
    while i < a.__len__():  # «<», «>», «.», «[», «]»
        if a[i] == '+':
            l[p] += 1
        elif a[i] == "-":
            l[p] -= 1
        elif a[i] == '.':
            print(l[p])
        elif a[i] == '<':
            l.insert(0, 0)
        elif a[i] == '>':
            p += 1
            if p >= l.__len__():
                l.reverse()
                l.insert(0, 0)
                l.reverse()
        elif a[i] == '[':
            if l[p] == 0:
                while a[i] != "]":
                    i += 1
            else:
                code(l, p, a[i + 1:])
                i -= 1
        elif a[i] == ']':
            i += 1
            break
        i += 1
    return l


a1 = input()
code([0], 0, a1)