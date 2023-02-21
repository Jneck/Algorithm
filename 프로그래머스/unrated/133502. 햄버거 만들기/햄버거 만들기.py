def solution(ingredient):
    stack_list = []
    answer = 0
    for i in ingredient:
        # 일단 스택 리스트에 3개는 있어야 말이 됨
        if len(stack_list) > 2:
            # 일단 빵 아니면 쌓음
            if i != 1:
                stack_list.append(i)
                
            # 빵인데 앞에 세트 다 있을 때 -> 햄버거 완성
            elif stack_list[-3:] == [1,2,3]:
                stack_list.pop()
                stack_list.pop()
                stack_list.pop()
                answer += 1
                
            # 빵인데 앞에 세트 부족하면 집어넣기:
            else:
                stack_list.append(i)
        else:
            stack_list.append(i)
            
    return answer