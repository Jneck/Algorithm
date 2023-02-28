import copy
def solution(board):
    # 위험지역 표시할 새로운 보드 생성
    n = len(board)
    safe_area = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            # 지뢰 발견시 1로 safe_area 대체
            if board[i][j] == 1:
                for x in range(-1,2,1):
                    for y in range(-1,2,1):
                        x_idx, y_idx = i+x, j+y
                        if (x_idx >= 0) & (y_idx >= 0):
                            try:
                                safe_area[x_idx][y_idx] = 1
                            except:
                                pass
    cnt = 0
    for s in safe_area:
        cnt += s.count(1)
        
    return n*n - cnt