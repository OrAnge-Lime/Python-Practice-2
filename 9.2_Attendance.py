m = int(input())
attendanceList = []
for i in range(m):
    n = int(input())
    if i == 0:
        for j in range(n):
            attendanceList.append(input())
    else:
        a1 = []
        for j in range(n):
            a1.append(input())

        for i in attendanceList:
            if not a1.__contains__(i):
                attendanceList.remove(i)

print(attendanceList)

