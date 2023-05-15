def solution(s):
    x = ''
    cnt_x = 0
    cnt_not_x = 0
    answer = 0
    while len(s) > 0:
        x = s[0]
        for idx, char in enumerate(s):
            if char == x:
                cnt_x += 1
            else:
                cnt_not_x += 1
            if cnt_x == cnt_not_x or idx == len(s)-1:
                cnt_x = 0
                cnt_not_x = 0
                s = s[idx+1:]
                answer += 1
                break
    return answer