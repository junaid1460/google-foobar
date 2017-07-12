

def getCoord(e):
    return int(e/8),e%8

def getval(i,j):
    return i*8+j

def getMoves(pos):
    i, j = getCoord(pos)
    moves = {}
    val = isvalid(i-1,j-2)
    if val is not None:
        moves[val]=1
    val = isvalid(i-2,j-1)
    if val is not None:
        moves[val]=1
    val = isvalid(i+1,j-2)
    if val is not None:
        moves[val]=1
    val = isvalid(i+2,j-1)
    if val is not None:
        moves[val]=1
    val = isvalid(i-2,j+1)
    if val is not None:
        moves[val]=1
    val = isvalid(i+2,j+1)
    if val is not None:
        moves[val]=1
    val = isvalid(i-1,j+2)
    if val is not None:
        moves[val]=1
    val = isvalid(i+1,j+2)
    if val is not None:
        moves[val]=1
    return moves

def isvalid(i,j):
    if i >=0 and j >=0 and i<=7 and j<=7:
        return getval(i,j)
    else:
        return None




def answer(src,dst):
    nodes = [e for e in range(64)]
    distances = { e:getMoves(e) for e in range(64)}
    

    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = src
    currentDistance = 0
    unvisited[src] = 0

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    return visited[dst]




print answer(0,1)