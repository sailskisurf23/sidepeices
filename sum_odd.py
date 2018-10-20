def size_triangle(n):
    result = 0
    for i in range(n+1):
        result += i
    return result


def size_triangle2(n):
    return sum(range(n+1))

def sum_odd(n):
    top = sum(range(n+1)) * 2
    return sum(list(range(1,top,2))[-n:])



print(sum_odd(4))
