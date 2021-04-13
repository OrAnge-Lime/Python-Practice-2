import copy


def plus(l, a2, a3):
    for i in range(l.__len__()):
        if a3 == l[i][0]:
            l[i][1] += a2
            if l[i][2] != 0:
                plus(l, a2, l[i][2])
    return l


a = int(input())
l = []
for i in range(a):
    b = input()
    if b.__contains__("опубликовал пост, количество просмотров:"):
        a1 = b.split(" ")[0]
        a2 = int(b.split(":")[-1])
        a3 = None
        l.append([a1, a2, a3])
    elif b.__contains__("отрепостил пост у"):
        a1 = b.split(" ")[0]
        a2 = int(b.split(":")[-1])
        a3 = b.split("отрепостил пост у ")[1].split(",")[0]
        l.append([a1, a2, a3])
        plus(l, a2, a3)


print(l)
