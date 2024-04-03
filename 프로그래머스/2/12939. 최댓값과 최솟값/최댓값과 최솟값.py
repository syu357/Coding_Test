def solution(s):
    answer = ''
    
    list_s = list(map(int, s.split()))
    
    return str(min(list_s)) + " " + str(max(list_s))