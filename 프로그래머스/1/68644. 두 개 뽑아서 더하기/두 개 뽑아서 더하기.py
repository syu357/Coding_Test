def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in answer: # 중복 제거
                answer.append(numbers[i] + numbers[j])

    answer.sort() # 정렬
             
    return answer