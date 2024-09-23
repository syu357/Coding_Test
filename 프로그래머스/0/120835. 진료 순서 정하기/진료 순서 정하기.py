def solution(emergency):
    answer1 = []
    answer2 = []
    
    answer2 = sorted(emergency, reverse=True) # 내림차순 정렬
    
    for i in emergency:
        answer1.append(answer2.index(i) + 1) # 우선순위 = 내림차순 정렬한 원소의 인덱스 값 + 1 
    
    return answer1