def solution(answers):
    score = [0] * 3 # 점수 배열
    
    no1 = [1, 2, 3, 4, 5] # 1번 수포자가 찍는 방식
    no2 = [2, 1, 2, 3, 2, 4, 2, 5] # 2번 수포자가 찍는 방식
    no3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자가 찍는 방식
    
    for i, answers in enumerate(answers):
        if answers == no1[i % len(no1)]: # 답이 같으면
            score[0] += 1 # 점수 +1
        if answers == no2[i % len(no2)]:
            score[1] += 1
        if answers == no3[i % len(no3)]:
            score[2] += 1
    
    result = [] 
    for j, s in enumerate(score):
        if s == max(score): # 동점자가 있으면
            result.append(j+1) # 결과 리스트에 추가
    
    return result