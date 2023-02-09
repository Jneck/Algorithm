def solution(X, Y):
    answer = ''
    x_num_dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    y_num_dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in X:
        x_num_dic[ord(i)-48] += 1
    for i in Y:
        y_num_dic[ord(i)-48] += 1

    print(x_num_dic[0])
    for i in range(9, -1, -1):
        if x_num_dic[i] > y_num_dic[i]:
            for k in range(y_num_dic[i]):
                answer += str(i)
        else:
            for k in range(x_num_dic[i]):
                answer += str(i)

    if len(answer) == 0:
        return '-1'

    if answer.count('0') == len(answer):
        return '0'

    return answer