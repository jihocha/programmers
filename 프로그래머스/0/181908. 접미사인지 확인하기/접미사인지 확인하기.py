def solution(my_string, is_suffix):
    return int(my_string[::-1][:len(is_suffix)] == is_suffix[::-1])