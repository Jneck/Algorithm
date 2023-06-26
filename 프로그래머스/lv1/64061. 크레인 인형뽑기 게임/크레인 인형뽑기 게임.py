def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for square in board:
            if square[move-1] > 0 :
                if len(bucket) > 0:
                    if bucket[-1] == square[move-1]:
                        bucket.pop()
                        answer += 2
                        square[move-1] = 0
                        break
                bucket.append(square[move-1])
                square[move-1] = 0
                break
    return answer