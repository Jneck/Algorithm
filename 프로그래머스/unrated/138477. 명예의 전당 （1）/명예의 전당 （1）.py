def solution(k, score):
    answer = []
    min_score = 2001
    
    if k < len(score):
        # 전당이 다 차지 않았을 때
        for i in range(k):
            if score[i] < min_score:
                min_score = score[i]
            answer.append(min_score)

        # 전당이 다 찼을 때
        tmp_list = score[:k]
        tmp_list.sort()
        for i in range(k,len(score)):
            if tmp_list[0] < score[i]:
                tmp_list[0] = score[i]
                tmp_list.sort()
            answer.append(tmp_list[0])
    else:
        # 전당이 다 차지 않았을 때
        for i in range(len(score)):
            if score[i] < min_score:
                min_score = score[i]
            answer.append(min_score)

    return answer