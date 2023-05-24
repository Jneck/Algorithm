def solution(cards1, cards2, goal):
    cards1Idx = 0
    cards2Idx = 0
    for word in goal:
        isWord = False
        if len(cards1) > cards1Idx:
            if cards1[cards1Idx] == word:
                cards1Idx += 1
                isWord = True
        if len(cards2) > cards2Idx:
            if cards2[cards2Idx] == word:
                cards2Idx += 1
                isWord = True
        if not isWord:
            return 'No'
    return 'Yes'