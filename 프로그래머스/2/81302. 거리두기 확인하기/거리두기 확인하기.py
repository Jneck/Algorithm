from collections import deque
def solution(places):
    answer = []
    # 각 시험자가 앉아있는 곳에서 맨하탄 거리 2까지 완전탐색
    direct_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    for place in places:
        is_0 = False
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    # 완전탐색
                    v_list = [[False for j in range(5)] for i in range(5)]
                    v_list[r][c] = True
                    dq = deque()
                    dq.append([r, c, 0])
                    while dq and not is_0:
                        cur_node = dq.popleft()
                        if cur_node[2] == 2:     # 2까지만 탐색 그 이상은 패스
                            continue
                        for i in range(4):
                            new_r = cur_node[0] + direct_list[i][0]
                            new_c = cur_node[1] + direct_list[i][1]
                            if new_r >= 0 and new_c >= 0 and new_r < 5 and new_c < 5:
                                if v_list[new_r][new_c] == False and place[new_r][new_c] != 'X':
                                    if place[new_r][new_c] == 'P':      # 거리두기가 지켜지지 않으면
                                        is_0 = True
                                        print(r, c, new_r, new_c)
                                        break
                                    v_list[new_r][new_c] = True
                                    dq.append([new_r, new_c, cur_node[2] + 1])
        answer.append(0 if is_0 else 1)
                            
    return answer