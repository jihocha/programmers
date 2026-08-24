def solution(arr, query):
    cnt = 0
    for i in query:
        cnt += 1
        if cnt % 2 != 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
    return arr