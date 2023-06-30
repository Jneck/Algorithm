def solution(survey, choices):
    answer = ''
    mbti_dict = {'R': 0, 'C': 0, 'J': 0, 'A': 0, 'T': 0, 'F': 0, 'M': 0, 'N': 0}
    for i in range(len(survey)):
        choice = choices[i]
        if choice == 4:
            continue
        elif choice < 4:
            mbti_dict[survey[i][0]] += (4-choice)
        elif choice > 4:
            mbti_dict[survey[i][1]] += (choice-4)
    if mbti_dict['R'] < mbti_dict['T']:
        answer += 'T'
    else:
        answer += 'R'
    if mbti_dict['C'] < mbti_dict['F']:
        answer += 'F'
    else:
        answer += 'C'
    if mbti_dict['J'] < mbti_dict['M']:
        answer += 'M'
    else:
        answer += 'J'
    if mbti_dict['A'] < mbti_dict['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer