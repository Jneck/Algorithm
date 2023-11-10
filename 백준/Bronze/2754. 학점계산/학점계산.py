temp_str = input()
if temp_str[0] == 'F':
    print('0.0')
else:
    print(str(round((69-ord(temp_str[0])) + ((44 - ord(temp_str[1])) * 0.3 if temp_str[1] != '0' else 0.0), 1)))