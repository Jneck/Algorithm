from itertools import combinations

def solution(nums):
    cnt = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for combination in list(combinations(nums, 3)):
        number = sum(combination)
        isPrimeNumber = True
        for i in range(2, int(number**(1/2)) + 1):
            if (number % i) == 0:
                isPrimeNumber = False
                break
        if isPrimeNumber:
            cnt += 1

    return cnt