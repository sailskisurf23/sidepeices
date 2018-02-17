def divisor(number):
    divisors = []
    for x in range(1, (number+1)):
        if number % x == 0:
            divisors.append(x)
    return divisors

def prime(number):
    return len(divisor(number)) <= 2

def gap(g, m, n):
    primelist = []
    for x in range(m,n+1):
        if prime(x) == True:
            primelist.append(x)
    for i in range(len(primelist)-1):
        if primelist[i+1] - primelist[i] == g:
            return [primelist[i],primelist[i+1]]
    return None

print(gap(6,100,110))
