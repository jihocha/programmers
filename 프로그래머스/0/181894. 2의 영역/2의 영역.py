def solution(arr):
    try:
        idx1 = arr.index(2)
        if arr[len(arr)-1] == 2:
            return arr[idx1:]
        else:
            idx2 = arr[::-1].index(2)
            return arr[idx1:-idx2]
    except ValueError:
        return [-1]
        