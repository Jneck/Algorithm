def solution(k, m, score):
    answer = 0
    ### k값의 범위가 작으므로 score문 한 번만 돌기 위해 리스트에 개수로 저장

    # score값은 1부터 k까지 가능 -> 0부터 k-1까지 인덱스 필요
    k_list = []
    for i in range(k):
        k_list.append(0)

    # score값들을 한 번 돌면서 각 인덱스에 개수를 저장
    for s in score:
        k_list[s-1] = k_list[s-1] + 1

    # 큰 숫자부터 돌면서 큰 값들로 이루어진 사과를 상자 안에 넣기(큰 값들만 먼저 모아야 최대가 되므로)
    for i in range(k-1, -1, -1):
        # (i+1)*m의 값을 가지는 사과 박스 개수 (실제 사과 가격은 i+1임)

        i_box = k_list[i] // m

        # 합산
        answer += (i_box * m * (i+1))

        # 남은 사과 박스 개수
        if i != 0:
            # 마지막 남은 사과들이 아닐 땐 다음 인덱스로 넘김
            k_list[i-1] = k_list[i-1] + (k_list[i] % m)

    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))