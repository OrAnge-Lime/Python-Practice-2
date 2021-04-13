str = input()
num = input()
l = input()
n = "0123456789"
t = True
for i in range(num.__len__()):
    if not n.__contains__(num[i]):
        t = False
        break
if t:
    if l.__len__() == 1 and str.__len__() >= int(num):
        if str[int(num) - 1] == l:
            print("YES")
        else:
            print("NO")
    else:
        print("ERROR")
else:
    print("ERROR")


