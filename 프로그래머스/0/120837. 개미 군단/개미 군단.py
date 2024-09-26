def solution(hp):
    answer = 0
    
    ant_5 = hp // 5
    ant_3 = (hp % 5) // 3
    ant_1 = (hp % 5) % 3
    
    answer = ant_5 + ant_3 + ant_1
    
    return answer