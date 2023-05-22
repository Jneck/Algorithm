def solution(id_list, report, k):
    answer = []
    reportedDict = {}
    reportDict = {}
    banIds = []
    for userId in id_list:
        reportedDict[userId] = 0
        reportDict[userId] = []
    
    for r in report:
        tmp_list = r.split()
        if tmp_list[1] not in reportDict[tmp_list[0]]:
            reportDict[tmp_list[0]].append(tmp_list[1])
            reportedDict[tmp_list[1]] += 1

    for key, value in reportedDict.items():
        if value >= k:
            banIds.append(key)
    
    for userId in id_list:
        cnt = 0
        for banId in banIds:
            if banId in reportDict[userId]:
                cnt += 1
        answer.append(cnt)
            
    return answer