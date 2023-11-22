def solution(queue1, queue2):
    total_len = len(queue1) + len(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    # 무조건 다른 큐에 집어넣어야 하므로 사실상 원형 배열 -> 투 포인터
    total_list = [0 for i in range(total_len)]
    for i in range(len(queue1)):
        total_list[i] = queue1[i]
    for i in range(len(queue1), total_len):
        total_list[i] = queue2[i-len(queue1)]
    
    if (sum1 + sum2) % 2 == 1:
        return -1
    target = (sum1 + sum2) // 2
    
    # 투 포인터 구현
    s_idx = 0
    e_idx = len(queue2)
    cnt = 0
    for i in range(2 * total_len):
        if s_idx > e_idx:
            return -1
        elif s_idx + total_len <= e_idx-1:
            return -1
        else:
            if sum1 < target:
                sum1 += total_list[e_idx % total_len]
                sum2 -= total_list[e_idx % total_len]
                e_idx += 1
                cnt += 1
            elif sum1 > target:
                sum1 -= total_list[s_idx % total_len]
                sum2 += total_list[s_idx % total_len]
                s_idx += 1
                cnt += 1
            else:
                break
    else:
        return -1
    
    return cnt