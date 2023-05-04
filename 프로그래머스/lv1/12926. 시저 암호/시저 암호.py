def solution(s, n):
    answer = ''
    for i in s:
        num = ord(i)
        if num < 40:
            answer += i
        elif num < 95 :
            if num + n < 91:
                answer += chr(num + n)
            else:
                answer += chr(num + n - 26)
        else:
            if num + n < 123:
                answer += chr(num + n)
            else:
                answer += chr(num + n - 26)

    return answer