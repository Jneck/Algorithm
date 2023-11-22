import sys

def solution(s):
    result_len = s.count('{') - 1
    # 숫자를 인덱스로 사용하기 위해 주어진 원소 범위만큼(1이상 100000이하 자연수)
    cnt_list = [sys.maxsize for i in range(100001)] 
    temp_str = ""
    for i in range(len(s)):
        if s[i] == '}' and s[i-1] != '}':
            if cnt_list[int(temp_str)] == sys.maxsize:
                cnt_list[int(temp_str)] = 1
            else:
                cnt_list[int(temp_str)] += 1
            temp_str = ''
        elif s[i] == ',' and s[i-1] != '}':
            if cnt_list[int(temp_str)] == sys.maxsize:
                cnt_list[int(temp_str)] = 1
            else:
                cnt_list[int(temp_str)] += 1
            temp_str = ''
        elif s[i] != '{' and s[i-1] != '}' and s[i] != ',':
            temp_str += s[i]
            
    
    
    temp_list = []
    for i in range(100001):
        if cnt_list[i] != sys.maxsize:
            temp_list.append([cnt_list[i], i])
            
    temp_list.sort(reverse=True)
    answer = []
    for i in range(result_len):
        answer.append(temp_list[i][1])
            
    return answer