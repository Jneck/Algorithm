def solution(array, commands):
    answer = []
    for command in commands:
        tmpArray = array[command[0]-1:command[1]]
        tmpArray.sort()
        answer.append(tmpArray[command[2]-1])
    return answer