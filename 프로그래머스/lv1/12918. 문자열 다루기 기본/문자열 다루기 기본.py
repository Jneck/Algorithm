def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for char in s:
        if char not in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True