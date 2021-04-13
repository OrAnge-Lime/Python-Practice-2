a = int(input())
products = []
for i in range(a):
    products.append(input())

numofres = int(input())
resepts = dict()
for i in range(numofres):
    name = input()
    ing = int(input())
    ingredients = []
    for k in range(ing):
        ingredients.append(input())
    resepts[name] = ingredients

for i in resepts:
    yes = True
    for j in resepts[i]:
        if not products.__contains__(j):
            yes = False
    if yes:
        print(i)




