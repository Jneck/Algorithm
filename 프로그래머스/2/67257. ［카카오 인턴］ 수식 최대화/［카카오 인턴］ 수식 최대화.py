def solution(expression):
    answer = 0
    answer_list = []
    # 연산을 따로 구현할 수 없으니 +, -, * 모든 경우, 먼저 이거부터
    temp_str = ''
    
    # 초기화
    temp_list = []
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
            temp_list.append(temp_str)
            temp_str = ''
            temp_list.append(expression[i])
        else:
            temp_str += expression[i]
    temp_list.append(temp_str)
    temp_str = ''
    
    
    
    ### +, -, *
    temp_list1 = [temp_list[i] for i in range(len(temp_list))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) + int(temp_list1[i])))
            continue
        if temp_list1[i] == '+':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])       
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) - int(temp_list1[i])))
            continue
        if temp_list1[i] == '-':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) * int(temp_list1[i])))
            continue
        if temp_list1[i] == '*':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    answer_list.append(abs(int(temp_list2[0])))
    
    
    ### +, *, -
    temp_list1 = [temp_list[i] for i in range(len(temp_list))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) + int(temp_list1[i])))
            continue
        if temp_list1[i] == '+':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])       
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) * int(temp_list1[i])))
            continue
        if temp_list1[i] == '*':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    # 복사
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) - int(temp_list1[i])))
            continue
        if temp_list1[i] == '-':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    answer_list.append(abs(int(temp_list2[0])))
    
    ### -, +, *
    temp_list1 = [temp_list[i] for i in range(len(temp_list))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) - int(temp_list1[i])))
            continue
        if temp_list1[i] == '-':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])       
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) + int(temp_list1[i])))
            continue
        if temp_list1[i] == '+':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    # 복사
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) * int(temp_list1[i])))
            continue
        if temp_list1[i] == '*':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    answer_list.append(abs(int(temp_list2[0])))
    
    ### -, *, +
    temp_list1 = [temp_list[i] for i in range(len(temp_list))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) - int(temp_list1[i])))
            continue
        if temp_list1[i] == '-':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])       
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) * int(temp_list1[i])))
            continue
        if temp_list1[i] == '*':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) + int(temp_list1[i])))
            continue
        if temp_list1[i] == '+':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    answer_list.append(abs(int(temp_list2[0])))
    
    ### *, +, -
    temp_list1 = [temp_list[i] for i in range(len(temp_list))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) * int(temp_list1[i])))
            continue
        if temp_list1[i] == '*':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])       
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) + int(temp_list1[i])))
            continue
        if temp_list1[i] == '+':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    # 복사
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) - int(temp_list1[i])))
            continue
        if temp_list1[i] == '-':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
    answer_list.append(abs(int(temp_list2[0])))
    
    ### *, -, +
    temp_list1 = [temp_list[i] for i in range(len(temp_list))]
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) * int(temp_list1[i])))
            continue
        if temp_list1[i] == '*':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])       
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) - int(temp_list1[i])))
            continue
        if temp_list1[i] == '-':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    # 복사
    temp_list1 = [temp_list2[i] for i in range(len(temp_list2))]
    
    temp_list2 = []
    pass_bool = False
    prev_num = 0
    for i in range(len(temp_list1)):
        if pass_bool:
            pass_bool = False
            temp_list2.append(str(int(prev_num) + int(temp_list1[i])))
            continue
        if temp_list1[i] == '+':
            prev_num = temp_list2.pop()
            pass_bool = True
        else:
            temp_list2.append(temp_list1[i])
            
    answer_list.append(abs(int(temp_list2[0])))
                
    
    return max(answer_list)