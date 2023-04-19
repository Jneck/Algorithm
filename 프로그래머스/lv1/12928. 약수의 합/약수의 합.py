def solution(n):
    answer = 0
    if n != 0 and n != 1:
        for i in range(1, int(n**(1/2))+1):
            if n%i == 0:
                if n//i != i:
                    answer += i
                    answer += n//i
                else:
                    answer += i
                
    elif n == 1:
        answer = 1
    return answer