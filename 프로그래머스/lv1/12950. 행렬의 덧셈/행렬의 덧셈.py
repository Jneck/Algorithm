def solution(arr1, arr2):
    len_row = len(arr1)
    len_col = len(arr1[0])
    answer = []
    for r in range(len_row):
        answer.append([])
        for l in range(len_col):
            answer[r].append(arr1[r][l] + arr2[r][l])
    return answer