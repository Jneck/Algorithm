function solution(friends, gifts) {
    const giftScore = new Map()
    const giftRecord = new Map()
    friends.map(me => {
        giftScore.set(me, 0)
        friends.map((friend) => {
            giftRecord.set(`${me} ${friend}`, 0)
        })
    })
    
    gifts.map((gift) => {
        [sender, reciever]= gift.split(' ')
        giftScore.set(sender, giftScore.get(sender) + 1)
        giftScore.set(reciever, giftScore.get(reciever) - 1)
        
        giftRecord.set(gift, giftRecord.get(gift) + 1)
    })
    
    // 선물 계산하기
    const giftCount = new Map();
    friends.map((me) => {
        giftCount.set(me, 0);
        friends.map((friend) => {
            const myCount = giftCount.get(me)
            const sendCount = giftRecord.get(`${me} ${friend}`);
            const recieveCount = giftRecord.get(`${friend} ${me}`);
            if (sendCount === recieveCount) {
                if (giftScore.get(me) > giftScore.get(friend)) {
                    giftCount.set(me, myCount + 1)
                }
                return
            }
            if (sendCount > recieveCount) {
                giftCount.set(me, myCount + 1)
            }
        })
    })
    
    
    return Math.max(...giftCount.values());
}