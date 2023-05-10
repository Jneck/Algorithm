def solution(s):
    answer = []
    alphabet_list = []
    for i in range(26):
        alphabet_list.append(-1)
    
    for idx, char in enumerate(s):
        char_idx = ord(char) - 97
        if alphabet_list[char_idx] == -1:
            answer.append(-1)
            alphabet_list[char_idx] = idx
        else:
            answer.append(idx - alphabet_list[char_idx])
            alphabet_list[char_idx] = idx
        
    return answer