def solution(left, right):
    # 약수 개수 홀수 -> 제곱수
    # left, right범위가 작으므로 제곱수 먼저 찾기 -> 1의 제곱부터 33의 제곱까지 -> 1089
    square_number_list = []
    for i in range(33):
        square_number_list.append((i + 1)**2)
    
    # left, right 위치 구해서 제곱수 리스트 자르기
    l_idx = 0
    r_idx = 0
    is_not_left_check = True
    for idx, s_num in enumerate(square_number_list):
        if is_not_left_check & (s_num >= left):
            l_idx = idx
            is_not_left_check = False
        if s_num <= right:
            r_idx = idx
    
    # left부터 right까지 전체 합 구한 뒤 자른 제곱수합 곱하기 2해서 빼줌
    return (left+right)*(right-left+1)/2 - 2*sum(square_number_list[l_idx:r_idx+1])
