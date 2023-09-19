import sys
input = sys.stdin.readline

S, P = map(int,input().split())
big_dna_str = input()
given_acgt_list = list(map(int,input().split()))
acgt_list = [0, 0, 0, 0]
cnt = 0
for idx in range(S):
    dna_char = big_dna_str[idx]
    if dna_char == 'A':
        acgt_list[0] += 1
    elif dna_char == 'C':
        acgt_list[1] += 1
    elif dna_char == 'G':
        acgt_list[2] += 1
    elif dna_char == 'T':
        acgt_list[3] += 1
    if idx >= P:
        if big_dna_str[idx-P] == 'A':
            acgt_list[0] -= 1
        elif big_dna_str[idx-P] == 'C':
            acgt_list[1] -= 1
        elif big_dna_str[idx-P] == 'G':
            acgt_list[2] -= 1
        elif big_dna_str[idx-P] == 'T':
            acgt_list[3] -= 1
    if idx >= P-1:
        is_correct = True
        for i in range(len(acgt_list)):
            if given_acgt_list[i] > acgt_list[i]:
                is_correct = False
                break
        if is_correct:
            cnt += 1
print(cnt)