def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        binaryStr = bin(a1 | a2)[2:]
        row = ('0' * (n - len(binaryStr)) + binaryStr)
        mapStr = ''
        for r in row:
            if r == '0':
                mapStr += ' '
            elif r == '1':
                mapStr += '#'
        answer.append(mapStr)
    return answer