inf = 999999999999999
def answer(entrances, exits, w):
    
    l = len(w)
    w.append([0 for i in range(l)])
    # w.append([0 for i in range(l)])
    c = len(w)
    for i in range(c):
        w[i] +=[0]
    for i in entrances:
        w[c-1][i] = inf
    pt = {}
    for i, e in enumerate(exits):
        pt[e] = True
    # for i in exits:
    #     w[i][c-1] = inf
    # for i in w:
    #     print i

    values = {}
    
    print
    count = 0
    width = [[w[i][j] if w[i][j] > 0 else -inf if i!=j else 0 for j in range(c)] for i in range(c)]
    next = [[None for i in range(c)] for j in range(c)]
    for k in range(c):
        for i in range(c):
            for j in range(c):
                m = min(width[i][k], width[k][j])
                if width[i][j] < m:
                    width[i][j] = m
                    next[i][j] = k
    

    for i in width:
        print i
    print
    for i in next:
        print i
    wmax =  width[c-1][e]
    print wmax

    for i in w:
        print i
    for i,_ in pt.iteritems():
        print width[c-1][i]
        path =  [c-1] + trace_path(width,next, c-1, i) +[i]
        print path
    prev = None
    for p in path:
        if prev is not None:
            w[prev][p] -= wmax
        prev = p
    count += wmax
    print count


def trace_path(w, n, i, j):
    if w[i][j] == -inf:
        return []
    k = n[i][j]
    if k == None:
        return []
    else:
        l = trace_path(w, n, i, k)  
        m =  trace_path(w, n, k, j)
        k = [k]
        if l != None:
           k  = l + k

        if m != None:
            k += m
        return k

# entrances = [0, 1]
# exits = [6, 7]
# path = [
# #  0  1  2  3  4  5  6  7
#   [0, 0, 2, 0, 0, 0, 0, 0], # 0
#   [0, 0, 3, 0, 0, 0, 0, 0], # 1
#   [0, 0, 0, 0, 4, 0, 0, 0], # 2
#   [0, 0, 0, 0, 0, 3, 1, 0], # 3
#   [0, 0, 0, 0, 0, 2, 4, 0], # 4
#   [0, 0, 0, 0, 0, 0, 3, 2], # 5
#   [0, 0, 0, 0, 0, 0, 0, 0], # 6
#   [0, 0, 0, 0, 0, 0, 0, 0], # 7
# ]

# def find_path(width, i, j):
#     pass

# entrances = [0]
# exits = [3]
# path = [[0, 3, 4, 0], 
#         [0, 0, 0, 3], 
#         [0, 0, 0, 2],
#         [9, 0, 0, 0]]


# entrances = [0, 1]
# exits = [4, 5]
# path = [
#   [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
#   [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
#   [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
#   [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
#   [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
#   [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
# ]


# entrances = [0]
# exits = [3]
# path = [[0, 7, 0, 0], 
#         [0, 0, 6, 0], 
#         [0, 0, 0, 8], 
#         [9, 0, 0, 0]]
entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]
answer(entrances,exits,path)