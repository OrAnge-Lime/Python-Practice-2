a = int(input())
b = int(input())
homelist = []

for i in range(a):
    homelist.append(input())
for j in range(b):
    book = input()
    if homelist.__contains__(book):
        print("YES")
    else:
        print("NO")


