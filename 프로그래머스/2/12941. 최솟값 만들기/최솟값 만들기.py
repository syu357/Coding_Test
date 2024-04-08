def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
        
    return sum