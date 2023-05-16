def solution(number, limit, power):
    tmp_list = []
    for i in range(1, number+1):
        cnt = 0
        for k in range(1, int(i**(1/2))+1):
            if i % k == 0:
                if (i // k) == k:
                    cnt += 1
                else:
                    cnt += 2
        tmp_list.append(cnt)
    
    for idx in range(len(tmp_list)):
        if tmp_list[idx] > limit:
            tmp_list[idx] = power
    return sum(tmp_list)