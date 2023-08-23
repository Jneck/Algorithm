def solution(array, n):
    difference = 101
    answer = 101
    for num in array:
        if abs(num - n) < difference:
            answer = num
            difference = abs(num - n)
        elif abs(num - n ) == difference:
            if answer > num:
                answer = num
                difference = abs(num - n)
    return answer