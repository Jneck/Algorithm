temp_list = [[] for i in range(2)]
for i in range(3):
    a, b = map(int, input().split())
    temp_list[0].append(a)
    temp_list[1].append(b)

for i in range(2):
    for j in range(3):
        if temp_list[i].count(temp_list[i][j]) == 1:
            print(temp_list[i][j] ,end = ' ')
            break

