def solution(a, b, c, d):
    dice = [a, b, c, d]
    count = {x: dice.count(x) for x in set(dice)}
    
    if len(count) == 1:
        return 1111 * a
    elif len(count) == 2:
        
        if 3 in count.values():
            p = max(count, key=count.get)
            q = min(count, key=count.get)
            return (10 * p + q) ** 2
        else:
            p, q = count.keys()
            return (p + q) * abs(p - q)
        
    elif len(count) == 3:
        p = [k for k, v in count.items() if v == 2][0]
        q, r = [k for k, v in count.items() if v == 1]
        return q * r
    else:
        return min(a, b, c, d)
    
    
    return answer