function solution(arr)
{
    var answer = [];
    
    for (const number of arr) {
        if (answer[answer.length-1] != number) {
            answer.push(number)
        }
    }

    return answer;
}