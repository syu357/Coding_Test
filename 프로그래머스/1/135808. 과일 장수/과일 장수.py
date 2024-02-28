def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) #최대 이익을 위해 내림차순으로 정렬
    
    box = []
    for i in range(0, len(score), m):
        if len(score) - m >= i: #상자의 개수(m)에 사과가 꽉차게 들어갈 경우만
            box.append(score[i:i+m]) #상자에 m개씩 사과를 담음

    for j in box:
        answer += min(j) * m #사과의 최소 가격과 개수를 곱해 최대 이익을 구함
    
    return answer