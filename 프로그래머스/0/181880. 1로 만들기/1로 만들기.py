def solution(num_list):
    answer = 0
    for i in num_list:
        count = 0
        while i != 1:
            i = i // 2
            count += 1
        
        answer += count
        
    return answer