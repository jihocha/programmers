from itertools import product
import numpy as np

def solution(n, s):
    if s < n:
        return [-1]
    Quo = [s // n] * n
    answer = [x + 1 if i >= len(Quo) - (s % n) else x for i, x in enumerate(Quo)]
    return answer
    
#    data = product(list(range(1, s + 1)), repeat = n)
#    tup_list = []
#    multi_list = []
    
#    for i in data:
#        if sum(i) == s:
#            tup_list.append(i)
#            multi_list.append(np.prod(i))
#    try:
#        return list(tup_list[(np.argmax(multi_list))])
#    except ValueError:
#        return [-1]
