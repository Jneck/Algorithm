from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_time = 0
    que = deque(truck_weights)
    bridge = deque()
    result = []
    if len(truck_weights) == 1:
        answer = bridge_length + 1
        return answer
    
    
    while que:
        if weight >= que[0]:
            # 1초 뒤 트럭이 나가는지 판단
            if bridge:
                exit_truck = bridge.popleft()
                if answer == exit_truck[1]:
                    weight += exit_truck[0]
                else:
                    bridge.appendleft(exit_truck)
                
            
            truck = que.popleft()
            weight -= truck
            # 다음 트럭이 다리에 출입 가능한 절대 시각(다리의 마지막 부분에 도달할 시각)과 함께 삽입
            bridge.append([truck, answer + bridge_length])
            answer += 1
        else:   # 다리에 트럭이 진입할 수 없을 경우 들어갈 수 있을때까지로 빨리감기
            exit_truck = bridge.popleft()
            weight += exit_truck[0]
            answer = exit_truck[1]
            
    answer += bridge_length
    
    return answer