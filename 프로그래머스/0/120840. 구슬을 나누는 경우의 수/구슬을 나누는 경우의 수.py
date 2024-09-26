# import itertools
import math

def solution(balls, share):
    answer = ''
    # 3C2 / 5C3 조합문제
    
#     nCr = itertools.combinations(balls, share) # combinations(리스트, 개수)여야 사용 가능
    
#     answer = nCr.len()

    # 즉, 조합 공식을 풀어서 코드로 작성해야함
    answer = math.factorial(balls) / (math.factorial(balls - share) * math.factorial(share))
    
    return answer