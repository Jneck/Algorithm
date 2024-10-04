function solution(progresses, speeds) {
    var answer = [];
    
    let curDay = 0;
    progresses.map((progress, idx) => {
        const needDay = Math.ceil((100 - progress) / speeds[idx])
        if (curDay < needDay) {
            curDay = needDay
            answer.push(1)
        }
        else {
            answer[answer.length - 1] += 1
        }
    })
    
    return answer;
}