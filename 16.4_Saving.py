n = int(input())
table = []
for i in range(n-1):
    k = input().split(" ")
    table.append(k)

way = input().split(" ")
station = way[0]
way.sort()

cheapest_way = table[int(way[1])-1][int(way[0])]

for i in range(table.__len__()):
    if i != int(way[1])-1:
        way1 = [int(way[0]), i+1]
        way1.sort()
        way1_len = table[int(way1[1])-1][int(way1[0])]

        way2 = [i+1, int(way[1])]
        way2.sort()
        way2_len = table[int(way2[1]) - 1][int(way2[0])]

        if int(cheapest_way) > int(way1_len) + int(way2_len):
            cheapest_way = int(way1_len) + int(way2_len)
            station = i+1

print(station)
