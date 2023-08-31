def solution(score):
    answer = [0] * len(score)
    sum_list = []
    for idx, s in enumerate(score):
        sum_list.append([idx,sum(s)])
    tmp_list = sorted(sum_list, reverse = True, key = lambda x: x[1])
    prev_rank = 0
    prev_num = 0
    for i in range(len(tmp_list)):
        if prev_num == tmp_list[i][1]:
            answer[tmp_list[i][0]] = prev_rank
        else:
            prev_rank = i + 1
            answer[tmp_list[i][0]] =prev_rank
            prev_num = tmp_list[i][1]
        
    return answer