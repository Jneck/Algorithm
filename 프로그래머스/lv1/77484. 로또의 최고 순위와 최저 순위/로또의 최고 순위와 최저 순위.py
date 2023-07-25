def solution(lottos, win_nums):
    cnt = 0
    for lotto_num in lottos:
        if lotto_num in win_nums:
            cnt += 1
    min_cnt = cnt
    max_cnt = cnt + lottos.count(0)
    return [7-max_cnt if max_cnt > 1 else 6, 7-min_cnt if min_cnt > 1 else 6]