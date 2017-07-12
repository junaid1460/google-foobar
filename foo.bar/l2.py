def answer(n = 1):
    fib = [1]
    total  = 2
    i = 0
    j = 1
    new  = 1
    while total <= n:
        fib += [new]
        new = fib[i] + fib[j]
        i += 1
        j += 1
        total += new

    tot = 0
    i = len(fib)
    for e in fib:
        tot+=e
    if(n-tot >= fib[i-1] + fib[i-2]):
        fib += [n-tot]
    # print tot, n-tot
    # print fib
    # print total
    # print len(fib)


    mult = []

    total = 1
    new = 1
    i = 0
    while total <= n:
        mult +=  [new]
        new  = mult[i] * 2
        total += new
        i += 1
    # print mult



    tot = 0
    for e in mult:
        tot += e
    # print total
    # print tot, n-tot, mult[i-1] + mult[i-2]
    if(n-tot >= mult[i-1] + mult[i-2]):
        mult += [n-tot]
    # print len(mult)
    # print((len(fib) - len(mult)))
    return len(fib) - len(mult)


print answer(917503)