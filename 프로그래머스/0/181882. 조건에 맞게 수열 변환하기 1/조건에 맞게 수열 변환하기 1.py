def solution(arra):
    next_arr = []
    for i in arra:
        if (i < 50) & (i % 2 != 0):
            next_arr.append(i * 2)
        elif (i >= 50) & (i % 2 == 0):
            next_arr.append(int(i / 2))
        else:
            next_arr.append(i)
    return next_arr