test = [1,2,3,4,5,6]

def answer(data = []):
    mc = {1:{},2:{},3:{}}
    for e in data:
        mct = {1:{},2:{},3:{},4:{}}
        for i in [1,2]:
            tot = 0
            for j in mc[i].iterkeys():
            
                if e % j == 0:
                    tot +=  mc[i][j]
            mct[i+1][e] = tot
        for i in [1,2,3]:
            for j,x in mct[i].iteritems():
                if mc[i].has_key(j):
                    mc[i][j] += x
                else:
                    mc[i][j] = x
                    

        if mc[1].has_key(e):
            mc[1][e] += 1
        else:
            mc[1][e] = 1

    count = 0
    for i,e in mc[3].iteritems():
        count += e
    return count
        

print answer([i for i in range(1,2001)])