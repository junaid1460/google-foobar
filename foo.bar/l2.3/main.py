import decimal
decimal.getcontext().prec = 309
def answer(n = ""):
    n = decimal.Decimal(n)
    # div = n.log10()/decimal.Decimal(2).log10() 
    # q = div % 1
    # if q > 0.5:
    #     div = div.to_integral_exact(rounding = decimal.ROUND_CEILING)
    # else:
    #     div = div.to_integral_exact(rounding = decimal.ROUND_FLOOR)
    count = 0
    while n > 1:
        print n, count
        if n % 2 == 1:
            tmp = (n + 1)/2
            if tmp % 2 == 0 :
                if n == 3:
                    n = n -1
                else:
                    n = n +1
                
            else:
                n  = n -1
            count += 1
            print n, count

        count += 1
        n = n/2
    print n, count
    return count

print(answer("91"))

