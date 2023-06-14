def solution(dartResult):
    answer = 0
    idx = 0
    prevScore = 0
    tmpStr = ''
    score = 0
    while idx < len(dartResult):
        if dartResult[idx] == 'S':
            score = int(tmpStr) ** 1
            tmpStr = ''
        elif dartResult[idx] == 'D':
            score = int(tmpStr) ** 2
            tmpStr = ''
        elif dartResult[idx] == 'T':
            score = int(tmpStr) ** 3
            tmpStr = ''
        elif dartResult[idx] == '*':
            answer += prevScore
            score = score*2
        elif dartResult[idx] == '#':
            score = -score
        else:
            answer += score
            prevScore = score
            score = 0
            tmpStr += dartResult[idx]
        idx += 1
        print(answer, tmpStr)
    answer += score
    return answer