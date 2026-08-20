def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1':
                answer += code[i] if i % 2 == 0 else ''
            else:
                mode += 1
        else:
            if code[i] != '1':
                answer += code[i] if i % 2 != 0 else ''
            else:
                mode -= 1
    return "EMPTY" if answer == '' else answer