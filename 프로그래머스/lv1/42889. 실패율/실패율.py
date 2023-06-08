def solution(N, stages):
    answer = []
    cnt = 0
    failDict ={}
    totalChallenger = len(stages)
    for i in range(1, N+1):
        currentRoundCnt = stages.count(i)
        currentChallenger = totalChallenger - cnt
        if currentChallenger == 0:
            failDict[i] = 0
        else:
            failDict[i] = currentRoundCnt / currentChallenger
        cnt += currentRoundCnt
    sorted_dict = sorted(failDict.items(), key = lambda item: (-item[1], item[0]))
    for a, b in sorted_dict:
        answer.append(a)
    return answer