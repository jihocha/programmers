def solution(arr, query):
    p1, p2 = 0, len(arr)
    
    for i, ind in enumerate(query):
        if i % 2 == 0:
            p2 = p1 + ind + 1
        else:
            p1 = p1 + ind
            
    return arr[p1:p2]