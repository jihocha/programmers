def solution(num_list):
    cnt = 0
    bool_list = []
    
    for i in num_list:
        cnt += int(i < 0)
            
    if cnt != 0:
        for i in num_list:
            bool_list.append(i < 0)
    else:
        return -1
        
    return bool_list.index(True)