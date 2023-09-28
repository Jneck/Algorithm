import sys
print = sys.stdout.write

N = int(input())

# 소수 판별 함수
def is_prime(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) < N:
        for i in range(1, 10, 2):
            new_num = num*10 + i
            if is_prime(new_num):
                dfs(new_num)
    else:
        print(str(num) + '\n')

dfs(2)
dfs(3)
dfs(5)
dfs(7)


