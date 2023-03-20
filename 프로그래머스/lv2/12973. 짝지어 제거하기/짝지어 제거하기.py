def solution(s):
    stack_list = []
    for char in s:
        if len(stack_list) == 0:
            stack_list.append(char)
        else:
            if stack_list[-1] == char:
                stack_list.pop()
            else:
                stack_list.append(char)
    return int(0 == len(stack_list))