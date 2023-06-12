def solution(answers):
    answerList = []
    person1 = [1, 2, 3, 4, 5, 0]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5, 0]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 0]
    
    for idx, answer in enumerate(answers):
        if answer == person1[idx % 5]:
            person1[-1] += 1
        if answer == person2[idx % 8]:
            person2[-1] += 1
        if answer == person3[idx % 10]:
            person3[-1] += 1

    
    correctCnts = [person1[-1], person2[-1], person3[-1]]
    maxCorrect = max(correctCnts)
    for idx, correctCnt in enumerate(correctCnts):
        if maxCorrect == correctCnt:
            answerList.append(idx + 1)
            maxCorrect = correctCnt
    return sorted(answerList)