from itertools import combinations
def solution(numbers):
    tmp_list = []
    for l in list(combinations(numbers,2)):
        tmp_list.append(l[0] + l[1])
    
    return sorted(list(set(tmp_list)))