def solution(a, b, n):
    cnt = 0
    while n >= a :
        receivedCola = n//a * b
        n = receivedCola + n % a
        cnt += receivedCola
    return cnt