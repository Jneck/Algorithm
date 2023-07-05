def solution(rank, attendance):
    tmp_list = []
    cnt = 1
    while 3 > len(tmp_list):
        num = rank.index(cnt)
        if attendance[num]:
            tmp_list.append(num)            
        cnt += 1
    
    return tmp_list[0] * 10000 + tmp_list[1] * 100 + tmp_list[2]