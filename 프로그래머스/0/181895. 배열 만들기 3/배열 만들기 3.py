def solution(arr, iv):
    answer = []
    
    return arr[iv[0][0]:iv[0][1]+1] + arr[iv[1][0]:iv[1][1]+1]