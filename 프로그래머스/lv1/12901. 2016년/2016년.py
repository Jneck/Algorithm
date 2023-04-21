def solution(a, b):
    monthDict = {31: [1, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11], 29: [2]}
    weekList = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    
    # 금요일
    afterDay = b
    for item in monthDict.items():
        for month in item[1]:
            if month < a:
                afterDay += item[0]
    return weekList[afterDay%7]