def solution(n):
    answer = 0
    for i in range(2, n+1):
        isPrimeNum = True
        for k in range(2, int(i**(1/2))+1):
            if i % k == 0 :
                isPrimeNum = False
                break
        if isPrimeNum:
            answer += 1
        
    return answer