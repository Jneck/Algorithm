import sys
def solution(alp, cop, problems):
    answer = 0
    
    # 최대 알고력, 코딩력 구하기
    alp_req_max = 0
    for i in range(len(problems)):
        if alp_req_max < problems[i][0]:
            alp_req_max = problems[i][0]
    
    cop_req_max = 0
    for i in range(len(problems)):
        if cop_req_max < problems[i][1]:
            cop_req_max = problems[i][1]
    # 특정 알고력과 코딩력일 때 걸리는 최소 시간 DP
    DP = [[sys.maxsize for i in range(cop_req_max+1)] for j in range(alp_req_max+1)]
    # 기존에 가지고 있던 알고력, 코딩력이 필요치보다 클 경우는 그냥 초기값을 최대치로 설정
    alp = min(alp, alp_req_max)
    cop = min(cop, cop_req_max)
    DP[alp][cop] = 0
    
    for i in range(alp, alp_req_max+1):
        for j in range(cop, cop_req_max+1):
            # 모든 알고력, 코딩력의 경우의 수에 대해 공부했을 때와 기존에 문제를 풀어 도달했을 때와의 최소값 비교
            DP[i][j] = min(DP[i][j], DP[i-1][j] + 1, DP[i][j-1] + 1)
            
            # 현재 상태에서 풀 수 있는 모든 문제의 경우의 수를 풀어 이후 도달하는 DP의 최솟값 갱신
            for problem in problems:
                if problem[0] <= i and problem[1] <= j:     # 문제를 풀 수 있을 때
                    new_alp = min(alp_req_max, i + problem[2])      # 인덱스 최대값을 넘어가면 안되므로
                    new_cop = min(cop_req_max, j + problem[3])
                    DP[new_alp][new_cop] = min(DP[new_alp][new_cop], DP[i][j] + problem[4])
    return DP[alp_req_max][cop_req_max]