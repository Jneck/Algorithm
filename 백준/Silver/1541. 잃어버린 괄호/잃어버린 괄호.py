import sys
input = sys.stdin.readline

num_str_list = input().strip()

answer = 0
num_str = ''
is_plus = True
for num_char in num_str_list:
    if num_char != '+' and num_char != '-':
        num_str += num_char
    else:
        if is_plus:
            answer += int(num_str)
            num_str = ''
        else:
            answer -= int(num_str)
            num_str = ''
        if num_char == '-':
            is_plus = False

if is_plus:
    answer += int(num_str)
    num_str = ''
else:
    answer -= int(num_str)
    num_str = ''

print(answer)