inp = [1, 2,6,12]



def answer(l = []):
    count = 0
    length = len(l)
    if length <= 2 or length > 2000:
        return 0
    l.sort()
    ds = {}
    for i in range(1,10):
        ds[i] = []
    ds[1] = l
    for e in l:
        for i in range(2,10):
            if e % i == 0:
                ds[i] += [e]
    larr  = [len(ds[i]) for i in range(1,10)]
    counter = [0 for i in range(1,10)]

    rev = [i for i in range(1,10)]
    rev.reverse()
    for i in range(length - 2):
        if l[i] == 1 and l[i+1] == 1:
            count += length - (i + 2)
            continue
        # print l[i]
        for j in rev:
            if l[i] % j == 0:
                # print j
                counter[j] += 1
                for k in range(counter[j],larr[j]):
                    for m in rev:

                        if ds[j][k] % m == 0:
                            # print m

                            print larr[m],counter[m]
                            count += (larr[m] - counter[m])
                            counter[m] += 1
                            break
                break
    return count




print answer([i for i in range(1,2001)])