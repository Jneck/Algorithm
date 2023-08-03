N = input()
tmp_list = []
for i in range(int(N)):
    tmp_list.append(int(input()))
tmp_list = sorted(tmp_list)
for i in tmp_list:
    print(i)