def solution(num):
    answer = -1
    cnt = 0
    if num == 1:
        answer = 0
    else:
        for i in range(500):
            if num % 2 == 0 :
                num //= 2
            else:
                num = num*3 + 1

            cnt += 1
            if num == 1:
                answer = cnt
                break
    return answer