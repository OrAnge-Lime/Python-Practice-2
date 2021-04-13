n = input()
a = [" * ", "* *", "***", "* *", "* *"]
b = ["** ", "* *", "** ", "* *", "** "]
c = [" * ", "* *", "*  ", "* *", " * "]

for k in range(5):
    s = ""
    for i in range(n.__len__()):
        if n[i] == 'A':
            s += a[k] + " "
        elif n[i] == 'B':
            s += b[k] + " "
        else:
            s += c[k] + " "
    print(s)