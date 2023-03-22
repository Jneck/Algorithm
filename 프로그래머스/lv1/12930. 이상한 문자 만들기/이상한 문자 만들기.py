def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if i != ' ':
            if cnt % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
        else:
            answer += ' '
            cnt = -1
        cnt += 1
                
    return answer