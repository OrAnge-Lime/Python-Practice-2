str = input()
for i in range(0, str.__len__()):
    s = ''
    for j in range(0, str.__len__()-i):
        s += "о"
    if str.__contains__(s):
        break

print(s.__len__())
