def solution(rank, attendance):
    answer = 0
    answer = [(i, r) for i, (r, att) in enumerate(zip(rank, attendance)) if att]
    answer.sort(key = lambda x: x[1])
    answer_list = [i[0] for i in answer]
    
    return 10000 * answer_list[0] + 100 * answer_list[1] + answer_list[2]