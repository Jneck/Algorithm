def solution(players, callings):
    answer = []
    player = {string : i for i,string in enumerate(players)}
    for c in callings:
        pre,post = player[c] - 1,player[c]
        player[players[pre]] = post
        player[players[post]] = pre
        players[pre],players[post] = players[post],players[pre]
    return players