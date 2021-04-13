a = int(input())
list = []
for i in range(a):
    b = input()
    if b.__contains__("встала в очередь.") or b.__contains__("встал в очередь."):
        list.append(b.split(" ")[0])
    elif b.__contains__("хватит тут стоять, пошли отсюда."):
        list.remove(b.split(",")[0])
    else:
        list.insert(list.index(b.split("!")[0].split(" ")[-1]) - 1, b.split(" ")[2])

print(list)