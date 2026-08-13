def solution(my_string, m, c):
    d = int(len(my_string) / m)
    answer = ''
    
    for k in range(d):
        answer += my_string[m * k + c - 1]
    return answer