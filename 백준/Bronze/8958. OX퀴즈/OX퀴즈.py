cnt = input()
for i in range(int(cnt)):
    score = 0
    before_score = 0
    ox_str = input()
    for ox_char in ox_str:
        if ox_char == 'O':
            before_score += 1
            score += before_score
        else:
            before_score = 0
    print(score)
