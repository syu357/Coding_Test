def solution(s):
    
    words = s.split(" ") # split()과 split(" ")은 다름!!
    
    for i in range(len(words)):
        words[i] = words[i][:1].upper() + words[i][1:].lower()
    
    # print(*words) 
    
    return ' '.join(words)