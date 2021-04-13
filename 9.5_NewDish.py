a = int(input())
res = []
for i in range(a):
    res.append(input())

days = int(input())
dishes = []
for i in range(days):
    b = int(input())
    for k in range(b):
        dish = input()
        if res.__contains__(dish):
            res.remove(dish)

for i in res:
    print(i)
