def solution(s, skip, index):
    answer = ''
    tmp_list = []
    for i in range(97, 123):
        alphabet = chr(i)
        if alphabet not in skip:
            tmp_list.append(alphabet)

    alphabet_len = len(tmp_list)
    for c in s:
        answer += tmp_list[(tmp_list.index(c) + index) % alphabet_len]

    return answer