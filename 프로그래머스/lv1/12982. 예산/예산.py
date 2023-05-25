def solution(d, budget):
    answer = 0
    sumD = sum(d)
    lenD = len(d)
    while budget < sumD:
        maxD = max(d)
        sumD -= maxD
        del d[d.index(maxD)]
        answer += 1
    return lenD - answer