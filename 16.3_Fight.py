n = int(input())
field = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    field.append(b)


num_of_k = int(input())
for i in range(num_of_k):
    x = int(input())
    y = int(input())

    for j in range(x-1, x+2):
        for k in range(y-1, y+2):
            if 0 <= j <= field.__len__() and 0 <= k <= field.__len__():
                field[j][k] -= 4
                if j == x and k == y:
                    field[j][k] -= 4


for i in range(field.__len__()):
    for j in range(field.__len__()):
        if field[i][j] < 0:
            field[i][j] = 0
    print(field[i])




