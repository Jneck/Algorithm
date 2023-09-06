N = int(input())
num_list = sorted(list(map(int, input().split())))

cnt = 0
for idx in range(len(num_list)):
    small_idx = 0
    big_idx = N-1
    while small_idx < big_idx:
        if small_idx == idx:
            small_idx += 1
            continue
        elif big_idx == idx:
            big_idx -= 1
            continue
        num_sum = num_list[small_idx] + num_list[big_idx]
        if num_sum < num_list[idx]:
            small_idx += 1
        elif num_sum > num_list[idx]:
            big_idx -= 1
        else:
            small_idx += 1
            big_idx -= 1
            cnt += 1
            break
print(cnt)