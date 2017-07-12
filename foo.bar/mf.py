def answer(m = "1", f = ""):
    import math
    m, f = int(m), int(f)
    if(m ==1 and m == f):
        return 0
    elif m==f:
        return "impossible"
    else:
        count = 0
        while(m != f and m != 0 and f !=0):
            shift = True if  m < f else False
            if(shift):
                if m == 1:
                    count += f - 1
                    f = 1
                else:
                    count += int(f/m)
                    f = f % m
            else:
                if f == 1:
                    count += m -1
                    m = 1
                else:
                    count += int(m/f)
                    m = m % f
        if(m ==1 and m == f):
            return str(count)
        else:
            return "impossible"
                
print answer("1","2")