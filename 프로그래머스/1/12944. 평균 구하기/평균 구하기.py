def solution(arr):

    sum = 0
    for i in arr:
        sum += i
    
    mean = sum / len(arr)
    
    return mean  