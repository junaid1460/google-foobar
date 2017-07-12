gcount = 0
import thread

def mod(l = []):
    length = len(l)
    if length <= 2 or length > 2000:
        return 0
    count = 0

    for i in range(length - 2):
        if l[i] == 1 and l[i + 1] == 1:
            count += length - (i + 2)
            continue
        for j in range(i+1,length -1):
            if(l[j]%l[i] == 0):
                for k in range(j+1,length):
                    if(l[k]%l[j] == 0):
                        count += 1
    global gcount
    thread.allocate_lock()
    gcount += count
    

def answer(l = []):
    els = []
    for e in l:
        found = True
        # print len(els)
        for i in range(len(els)):
            # print i,e
            if els[i][0] <= e:
                found = False
                els[i] =  [e] + els[i]
        if found :
            els.append([e])
    count = 0
    
    for e in els:
        # print(e)
        e.reverse()
        thread.start_new_thread(mod,(e,))
    while thread._count() > 0:
        pass
    global gcount
    return gcount
  

from random import randint
print answer([randint(0,999999) for i in range(1,2001)])
