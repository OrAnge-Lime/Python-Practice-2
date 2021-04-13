n = input().lower()
m = input().split(" ")

for i in range(m.__len__()):
    if m[i].__contains__(n) or m[i].__contains__(n.upper()):
        print(m[i])
