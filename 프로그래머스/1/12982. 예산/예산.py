def solution(d, budget):
    i = 1
    total = sorted(d)[0]
    if sum(d) <= budget:
        return len(d)
    else:
        while total < budget:
            total += sorted(d)[i]
            i += 1
        if total == budget:
            i += 1
        return i - 1