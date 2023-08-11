def solution(sides):
    answer = 0
    small_side = 0
    big_side = 0
    if sides[0] < sides[1]:
        small_side = sides[0]
        big_side = sides[1]
    else:
        small_side = sides[1]
        big_side = sides[0]
    tmp_list = []

    # 모르는 c가 가장 길 때
    # small_side + big_side > c >= big_side
    for i in range(big_side, small_side + big_side):
        tmp_list.append(i)

    # big_side가 가장 길고 c가 중간 사이즈일때
    # small_side + c > big_side >= c
    for i in range(big_side - small_side + 1, big_side + 1):
        tmp_list.append(i)
        
    # c가 가장 작은 사이즈일 때
    # small_side + c > big_side, small_side >= c
    for i in range(big_side - small_side + 1, small_side + 1):
        tmp_list.append(i)
    
    return len(set(tmp_list))