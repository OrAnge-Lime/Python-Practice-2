import math

n = int(input())
nn1 = []
nn2 = []
for i in range(n):
    nn1.append(input())
    nn2.append(int(input()))

final = []
for i in range(math.ceil(n/2)):
    p = nn2.index(max(nn2))
    final.append(nn1[p])
    nn2.remove(max(nn2))
    nn1.remove(nn1[p])

final.sort()
nn1.sort()

for i in range(final.__len__()):
    print(final[i])

for i in range(nn1.__len__()):
    print(nn1[i])

