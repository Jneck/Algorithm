def solution(num, k):
    answer = 0
    str_num = str(num)
    idx = str_num.find(str(k))
    if idx == -1:
        return -1
    else:
        return idx + 1