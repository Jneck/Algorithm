def solution(s):
    answer = ''
    tmp_list = list(map(int, s.split()))
    tmp_list.sort()
    answer = str(tmp_list[0]) + ' ' + str(tmp_list[-1])
    return answer