from __future__ import print_function
data = [1, 2, 3]

def answer(data, n):
    # your code here
    counts = {}
    #iterate and count occurences
    for i,e in enumerate(data):
        if e in counts:
            counts[e] += [i]
        else:
            counts[e] = [i]
    #for being version safe
    #idk which version you are using
    it = None
    #importing inside function, since i have no idea if
    #code outside this function will get executed or not
    import sys
    if(sys.version_info[0] == 3):
        #python 3
        it = counts.items()
    else:
        #python 2
        it = counts.iteritems()
    #setting values over n to None
    for _,e in it:
        if len(e) > n :
            for i in e:
                data[i] = None
    #referenced array will have Nones, so delete and append new data
    #select only those which aren't None
    tmp = [e for e in data if e is not None]
    del data[:]
    data += tmp
    return data
    

print(answer(data,1))
print(data)
