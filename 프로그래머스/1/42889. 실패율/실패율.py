# def solution(N, stages):
#     fail = {}
    
#     cnt_arr = [0] * (N + 2) # 도전자 수를 세는 배열    
    
#     for i in stages:
#         cnt_arr[i] += 1   
    
#     user = len(stages) # 사용자 수
    
#     for i in range(1, N+1): # 실패율 구하기        
#         if (user - cnt_arr[i-1]) == 0: # 분모가 0이면
#             fail[i] = 0 # 실패율 = 0
#         else:
#             fail[i] = cnt_arr[i] / (user - cnt_arr[i-1])
#             user -= cnt_arr[i-1]
        
#     print(fail)
    
#     result = sorted(fail, key=lambda x : fail[x], reverse=True)
        
#     return result

# 수정
def solution(N, stages):
    fail = {} # 스테이지 명, 실패율을 저장하는 딕셔너리
    cnt_arr = [0] * (N + 2) # 도전자 수를 세는 배열    
    
    for i in stages:
        cnt_arr[i] += 1   
    
    user = len(stages) # 사용자 수
    
    for i in range(1, N+1): # 실패율 구하기        
        if cnt_arr[i] == 0: # 도전자가 0이면
            fail[i] = 0 # 실패율 = 0
        else:
            fail[i] = cnt_arr[i] / user # 도전자 / 사용자
            user -= cnt_arr[i] # 사용자 -= 도전자
    
    result = sorted(fail, key=lambda x : fail[x], reverse=True) # 실패율을 기준으로 내림차순으로 저장
        
    return result
