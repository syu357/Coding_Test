def solution(s):
    answer = True  
         
    stack = [] 
    for i in s:
        if i == '(': # 여는 괄호면 stack에 push
            stack.append(i) 
        else: # i == ')', 닫는 괄호
            if len(stack) == 0: # stack이 비어있으면 (: 여는 괄호가 없으면)
                answer = False
            else:
                stack.pop() # stack에서 여는 괄호 pop
        
    if len(stack) != 0: # stack이 비어있지 않으면 (: 여는 괄호가 남았으면)
        answer = False 
        
    return answer