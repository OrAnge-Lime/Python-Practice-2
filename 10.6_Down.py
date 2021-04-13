s = input()
a = s[0]

str = ""
symb = 1
pr = 0
for i in range(1, s.__len__()):
    if s[i] == 'V':
        for j in range(pr):
            str += " "
        for j in range(symb):
            str += s[0]
        print(str)
        str = ""
        if s[i-1] == ">":
            pr = symb + pr - 1
        symb = 1
    elif s[i] == ">":
        symb += 1
    else:
        symb += 1
        pr -= 1

for j in range(pr):
    str += " "
for j in range(symb):
    str += s[0]
print(str)

