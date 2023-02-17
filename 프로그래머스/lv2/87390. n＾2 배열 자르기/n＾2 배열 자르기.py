def solution(n, left, right):
    answer = []
    # 1차원 배열 규칙. 1 1개 + 234~~~, 2 2개 345~~~, 3 3개 456 ~~, 4 4개 567~~~, ~~~
    
    # arr을 위 규칙에 맞게 필요한 부분만 제작
    for i in range(left//n, right//n+1):
        for j in range(n):
            # 위 규칙에 맞게 if else문 제작
            if j <= i:
                answer.append(i+1)
            else:
                answer.append(j+1)
    # 필요한 부분 행 위치
    loc = left%n
    return answer[loc: loc + (right-left+1)]