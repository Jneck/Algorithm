def solution(numbers):
    answer = 0
    number_dict={"one":1, "two":2, "three":3, "four":4, "five":5, 
                 "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
    
    for k, v in number_dict.items():
        # 파이썬 replace( ) 문자열을 변경하는 함수 (Python)
        # replace(old, new, [count])' 형식으로 사용한다.
        # - old : 현재 문자열에서 변경하고 싶은 문자
        # - new: 새로 바꿀 문자
        # - count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다. 기본값은 전체를 의미하는 count=-1로 지정되어있다. 
        numbers = numbers.replace(k, str(v))
    answer = int(numbers)
    return answer