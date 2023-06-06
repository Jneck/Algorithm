def solution(s):
    tmp_str = ''
    en_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    idx = 0
    while len(s) > idx:
        if (47< ord(s[idx])) & (ord(s[idx]) < 58):
            tmp_str += s[idx]
            idx += 1
            continue
        for key, value in en_dict.items():
            if len(s[idx:]) >= len(key):
                if s[idx:idx + len(key)] == key:
                    tmp_str += str(value)
                    idx += len(key)
                    break
    return int(tmp_str)