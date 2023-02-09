def solution(spell, dic):
    answer = 2
    for d in dic:
        canMakeSpell = True
        for s in spell:
            if s not in d:
                canMakeSpell = False
        if canMakeSpell:
            answer = 1
            break
    return answer