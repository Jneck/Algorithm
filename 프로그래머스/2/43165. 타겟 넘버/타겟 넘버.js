function solution(numbers, target) {
    var answer = 0;
    dfs(0, 0);
    
    return answer;

    
    function dfs(idx, curNum) {
        if(idx === numbers.length && curNum === target) {
            answer += 1;
            return;
        }
        if(idx === numbers.length) {
            return;
        }
        
        dfs(idx+1, curNum + numbers[idx])
        dfs(idx+1, curNum - numbers[idx])
    }
}