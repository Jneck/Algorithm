def solution(a, b, c, d):
    answer = 0
    num_list = [a, b, c, d]
    if num_list.count(a) == 4:
        return 1111*a
    elif num_list.count(a) == 3:
        for num in num_list:
            if num != a:
                return (10*a + num) ** 2
    elif num_list.count(a) == 2:
        tmp_list = []
        for num in num_list:
            if num != a:
                tmp_list.append(num)
        if tmp_list[0] == tmp_list[1]:
            return (a + tmp_list[0]) * abs(a - tmp_list[0])
        else:
            return tmp_list[0] * tmp_list[1]
    else:
        if num_list.count(b) == 3:
            return (10*b + a) ** 2
        elif num_list.count(b) == 2:
            if b == c:
                return a*d
            else:
                return a*c
        elif num_list.count(c) == 2:
            return a*b
        else:
            return min(num_list)
            
            
                
            
    return answer