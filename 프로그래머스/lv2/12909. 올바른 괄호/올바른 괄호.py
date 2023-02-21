def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    stack_list = []
    for i in s:
        stack_list.append(i)
        if stack_list[-2:] == ["(", ")"]:
            stack_list.pop()
            stack_list.pop()

    return len(stack_list) == 0