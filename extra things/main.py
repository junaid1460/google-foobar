# integer is better than float
sqrt = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
def prime(n):
    return (sqrt*n)//(10**100) #divmod 10 ^ 100 points backward to get exact floor(n * 0.414... )

def calc(n):
    if n <= 1:
        return n // 1
    prim = prime(n)
    # [1 * sqrt(2)] + [2 * sqrt(2)] + ...
    # [1 * 1.414..] + [2 * 1.414..] + ...
    # 1 + [1 * 0.414...] + 2 + [2 * 0.414...] + ..
    # (1 + 2 + 3 + 4 ... n) + ([1 * 0.414...] + [2 * 0.414..] + ..)
    # n ( n + 1 ) / 2 + ([1 * 0.414...] + [2 * 0.414..] + ..) etc 
    # finally found final derivation of this in stack network 
    return n*prim + n*(n+1)/2 - prim*(prim+1)/2 - calc(prim)

def answer(n):
    n = long(n)
    return format(calc(n))


print answer("77")