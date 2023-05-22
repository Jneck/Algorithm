def solution(park, routes):
    dog_x = 0
    dog_y = 0
    park_list = []
    # 초기 강아지 idx값 구하기, 속도를 위해 park를 리스트로 만들기
    for i, row in enumerate(park):
        tmp_list = []
        for j, r in enumerate(row):
            tmp_list.append(r)
            if r == 'S':
                dog_x = j
                dog_y = i
        park_list.append(tmp_list)

    for route in routes:
        n = int(route[2])
        # 인덱스 오류시 그냥 패스
        try:
            if route[0] == 'E':
                # 장애물 검증
                isObstacle = False
                for t in range(1, n+1):
                    if park_list[dog_y][dog_x+t] == 'X':
                        isObstacle = True
                if isObstacle:
                    continue
                    
                # 강아지 옮기기 및 좌표 최신화
                park_list[dog_y][dog_x+n] = 'S'
                park_list[dog_y][dog_x] = 'O'
                dog_x = dog_x+n
            
            elif route[0] == 'W':
                # 장애물 검증
                isObstacle = False
                for t in range(1, n+1):
                    if park_list[dog_y][dog_x-t] == 'X':
                        isObstacle = True
                if isObstacle:
                    continue
                    
                # 강아지 옮기기 및 좌표 최신화
                if dog_x-n < 0:
                    continue
                park_list[dog_y][dog_x-n] = 'S'
                park_list[dog_y][dog_x] = 'O'
                dog_x = dog_x-n
                
            elif route[0] == 'N':
                # 장애물 검증
                isObstacle = False
                for t in range(1, n+1):
                    if park_list[dog_y-t][dog_x] == 'X':
                        isObstacle = True
                if isObstacle:
                    continue
                    
                # 강아지 옮기기 및 좌표 최신화
                if dog_y-n < 0:
                    continue
                park_list[dog_y-n][dog_x] = 'S'
                park_list[dog_y][dog_x] = 'O'
                dog_y = dog_y-n
            
            elif route[0] == 'S':
                # 장애물 검증
                isObstacle = False
                for t in range(1, n+1):
                    if park_list[dog_y+t][dog_x] == 'X':
                        isObstacle = True
                if isObstacle:
                    continue
                    
                # 강아지 옮기기 및 좌표 최신화
                park_list[dog_y+n][dog_x] = 'S'
                park_list[dog_y][dog_x] = 'O'
                dog_y = dog_y+n
            
        except:
            pass
    
    # 최종 강아지 인덱스 구하기
    for i, row in enumerate(park_list):
        for j, r in enumerate(row):
            if r == 'S':
                dog_x = j
                dog_y = i
                break
                
    return [dog_y, dog_x]