def solution(str_list):
    answer = []
    l_idx = 21
    r_idx = 21
    if 'l' in str_list:
        l_idx = str_list.index('l')
    if 'r' in str_list:
        r_idx = str_list.index('r')
    if (l_idx + r_idx) == 42:
        return []
    if l_idx < r_idx:
        return str_list[:l_idx]
    else:
        return str_list[r_idx+1:]