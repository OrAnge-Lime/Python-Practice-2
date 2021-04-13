list = []
a = input()
while a != "":
    list.append(a.split(":"))
    a = input()

list2 = input().split(";") #12345;qwerty;password

for i in range(list.__len__()):
    if list2.__contains__(list[i][1]):
        print("To: " + list[i][0])
        print(list[i][4].split(",")[0] + ", ваш пароль слишком простой, смените его.")
