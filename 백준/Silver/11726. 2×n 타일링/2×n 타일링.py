import sys
sys.setrecursionlimit(10**6)
N = int(input())

DP = [0 for i in range(N+1)]
def call_dp(num):
    if DP[num] == 0:
        if num == 1:
            DP[1] = 1
            return DP[1]
        elif num == 2:
            DP[2] = 2
            return DP[2]
        else:
            DP[num] = (call_dp(num-2) + call_dp(num-1)) % 10007
            return DP[num]
    else:
        return DP[num]

print(call_dp(N))