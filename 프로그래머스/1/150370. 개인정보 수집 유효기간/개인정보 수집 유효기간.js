function solution(today, terms, privacies) {
    const termsObject = new Map()
    var answer = [];

    terms.map((term) => {
        [type, monthInterval] = term.split(' ')
        termsObject.set(type, monthInterval*28)
    })
    
    privacies.map((privacy, index) => {
        [startDate, type] = privacy.split(' ')
        if (termsObject.get(type) <= (getTime(today) - getTime(startDate))) {
            answer.push(index + 1)
        }
    })
    return answer;
}

function getTime(dateStr) {
    [y, m, d] = dateStr.split('.').map((num) => num.startsWith('0') ? parseInt(num.slice(1)) : parseInt(num))
    return  y*12*28 + m*28 + d
}