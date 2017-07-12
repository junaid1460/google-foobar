nodes = ('A', 'B', 'C', 'D', 'E', 'F','G')
# {0: {2: 4, 3: 6}, 1: {2: 5, 3: 2}, 2: {4: 4, 5: 4}, 3: {4: 6, 5: 6}, 4: {}, 5: {}}
distances = {
    'X': {'A':0,'B':0},
    'B': {'C': 5, 'D': 2},
    'A': {'C': 4, 'D':6},
    'D': {'E':6,'E':6},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': { 'E': 4, 'F': 4},
    'E': { 'G':0},
    'F': {'G':0},
    'G': {}
    }

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 'A'
currentDistance = 0
unvisited[current] = currentDistance

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

print(visited)