def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    tmp_id = ''
    # 2단계
    for char in new_id:
        ascii_char = ord(char)
        if (char == '-') or (char == '_') or (char == '.') or ((ascii_char >= 97) and (ascii_char <= 122)) or ((ascii_char >= 48) and (ascii_char <= 57)):
            tmp_id += char
    new_id = tmp_id
    # 3단계
    tmp_id = ''
    prev_char = '?'
    for char in new_id:
        if (prev_char == '.') and (char == '.'):
            continue
        prev_char = char
        tmp_id += char
    new_id = tmp_id  
    
    # 4단계
    while True:
        if len(new_id)>1:
            if new_id[0] == '.':
                new_id = new_id[1:]
            elif new_id[-1] == '.':
                new_id = new_id[:-1]
            else:
                break
        elif len(new_id) == 1:
            if new_id[0] == '.':
                new_id = []
                break
            else:
                break
        else:
            break
    
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while True:
            if new_id[-1] == '.':
                new_id = new_id[:-1]
            else:
                break
        
    # 7단계
    if len(new_id) <=2 :
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id