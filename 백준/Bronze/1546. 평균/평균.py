subject_cnt = input()
scores = list(map(int,input().split()))
max_score = max(scores)
new_scores = []
for score in scores:
    new_scores.append(score/max_score*100)
print(sum(new_scores)/int(subject_cnt))
