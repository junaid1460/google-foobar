# pairs of 2 where e[i] divides e[j] divides e[k] 
# and i < j < k

test = [1,2,3,4,5,6]

def answer(data = []):
    lookup = {}
    divisibles = []
    divisible_i = 0
    iter = 0
    prev = -1
    mc = {1:{},2:{},3:{},4:{}}
    for e in data:
        # if e == prev:
        #     lookup[e][len(lookup[e]) - 1][1] += 1
        #     continue
        # print e,
        
        addtolookup = {}
        print "------------------------------------------------------"
        print "at",e
        for i in range(len(divisibles)):
            # del divisibles[i][0]
            print i,divisibles[i]
        print "lookup"
        for i,x in lookup.iteritems():
            print i,x

        for i in 
        
        for i in lookup.iterkeys():

            if e % i == 0:
                for indexes in lookup[i]:
                    last = divisibles[indexes][0]
                    xx = divisibles[indexes][1]
                    if (e % last) == 0 and xx < 3:
                        divisibles.append([divisibles[indexes][0],divisibles[indexes][1]])
                        if not addtolookup.has_key(i):
                            addtolookup[i]= [iter]
                        else:
                            addtolookup[i]+=[iter]
                        iter+=1
                        divisibles[indexes][0] = e
                        divisibles[indexes][1] +=1

        # print "<add>"
        for i,x in addtolookup.iteritems():
            lookup[i] += x
        # print"</add>"
        
        divisibles.append([e,1])
        if mc[1].has_key(e):
            mc[1][e] += 1
        else:
            mc[1][e] = 1
        if not lookup.has_key(e):
           
            lookup[e] = [iter]
        else:
            lookup[e] += [iter]
        
        print "after",e
        for i in range(len(divisibles)):
            # del divisibles[i][0]
            print i,divisibles[i]
        print
        prev = e
        iter +=1





    print "\ndivisibles"
    c =0
    
    for i in range(len(divisibles)):
        # del divisibles[i][0]
        print i,divisibles[i]
        
    # print
    # print "lookup"
    # print
    count = 0
    for i,e in lookup.iteritems():
        print i,e
    for i in range(len(divisibles)):
        if  divisibles[i][1] == 3:
            count +=1

        # print 

    # count = 0
    
    return count


print answer([1,1,1,1])