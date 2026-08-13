def solution(q, r, code):
    answer = ''
    for k in range(r, len(code), q):
        answer += code[k]
    return answer