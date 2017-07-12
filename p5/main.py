# import matplotlib.pyplot as plt
dimensions = [3, 2]
captain_position = [1, 1]
badguy_position = [2, 1]
distance = 4


dimensions = [300, 275]
captain_position = [150, 150]
badguy_position = [180, 100]
distance = 501

import math
def between(length, val):
    return val, length - val
def getquad(x, y):
    if x == 0 or  y == 0:
        return 5
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y > 0:
        return  2
    else:
        return 3
def quad(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return 1
def answer(dim, player, enemy, distance):
    width = dim[0] 
    height = dim[1] 
    left, right = between(width, enemy[0])
    top, bottom = between(height, enemy[1])
    # print(left, right)
    # print(top, bottom)

    elm = [enemy]
    elp = [enemy]
    for i in range(2):
        l = len(elm)
        lel, rel = elm[0][:], elm[l-1][:]
        lel[0] -= abs(2*left)
        # print lel
        rel[0] += (2*right)
        # print rel
        elm = [lel] + elm
        elm += [rel]
        tmp = left
        left = right
        right = tmp
        # left, right = right, left
        l = len(elp)
        tel, bel = elp[0][:], elp[l-1][:]
        
        bel[1] -= abs(2 * bottom)
        tel[1] += abs(2 * top)
        elp = [tel] + elp + [bel]
        tmp = top
        top = bottom
        bottom  = tmp

    mat = [{} for i in range(7)]
    # print(elm)
    # print( elp)
    # print()
    x1 = player[0]
    y1 = player[1]
    temp = []
    for k, t in enumerate(elp):

        tmp = [i[:] for i in elm]
        # print k
      
        for j, e in enumerate(tmp):
            tmp[j][1] = elp[k][1]
            x = tmp[j][0]
            y = tmp[j][1]
            dist = math.hypot(y - y1, x-x1)
            q = quad(x - x1, y - y1)

            if q == 0:
                key = "undefined"
            else:
                key = str(math.atan2(y - y1,x - x1))
            if dist <= distance:
                print(x,y, dist)
                mat[q][key] = dist
            # else:
            #     print("rejected", dist)
                
        temp.append(tmp)
    # for i in mat:
    #     print(len(i))

    print temp
    for i in mat:
        print len(i)



 

        
   

answer(dimensions, captain_position, badguy_position, distance)