def solution(participant, completion):
    
    # 이름순으로 정렬
    ## ex) p : ["ana", "mislav", "mislav", "stanko"]
    ##     c : ["ana", "mislav", "stanko"]
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]: # 정렬한 이름순이 맞지 않으면
            return participant[i] # 완주하지 못한 사람 출력
            
    return participant[-1] # 정렬한 이름순이 다 맞았다면, 가장 마지막에 남은 사람 출력
    ## ex) p : ["eden", "kiki", "leo"]
    ##     c : ["eden", "kiki"]
    
    
    
#     ## 시간초과
#     # 동명이인이 있을 때 (set 활용 -> 중복제거)
#     if len(participant) != len(set(participant)):   
#         for i in participant:
#             if i in completion: 
#                 completion.remove(i)
#             else:
#                 return i    
    
#     # 동명이인이 없을 때
#     else:
#         for i in participant:  
#             if i not in completion: # 참가자 명단에는 있고 완주자 명단에 없으면
#                 return i
    
