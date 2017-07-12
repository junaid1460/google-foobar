import heapq
class Queue(object):
    def __init__(self):
        self.heap = []
    def push(self, el):
        heapq.heappush(self.heap, el)
    def pop(self):
        if len(self.heap) == 0:
            return None
        return heapq.heappop(self.heap)
    def __str__(self):
        str = ' { '
        for i in self.heap:
            str += i.__str__() + ","
        str += "}"
        return str
    def empty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False

class elm(object):
    def __init__(self, key, val):
        self.key = key
        self.value = val
    def __cmp__(self, el):
        v =  cmp(self.value, el.value)
        if v != 0:
            return -v
        return v
        
    def __str__(self):
        return str(self.key) + ":" + str(self.value)



infinity = 9999999

def dijkstra(graph, source):
    # print source
    if len(graph[source]) == 0:
        return None
    global infinity
    width = { i: -infinity for i in graph}
    prev = {}
    width[source] = infinity
    vt = Queue()
    vt.push(elm(source, infinity))
    while not vt.empty():
        current = vt.pop()
        el = []
        if current is not None:
            x = None
            while True:
                x = vt.pop()
                if x is not None:
                    el =  [x] + el
                    if x.value != current.value:
                        break
                else:
                    break
            for i in el:
                vt.push(i)
        # print "picked", current
        for v, e in graph[current.key].iteritems():
            m = max(width[v],min(width[current.key],e))
            if m > width[v]:
                width[v] = m
                prev[v] = current.key
                vt.push(elm(v, m))
                #normalize since in heap to 
                
    # print source, width
    
    # print prev
    return [width, prev]

        


    
def answer(entrances, exits, path):
    graph = {}
    
    global infinity
    for i, e in enumerate(path):
        graph[i] = {}
        for j, t in enumerate(e):
            if t > 0:
                graph[i][j] = t
    count = 0
    counts =  Queue()
    for i in entrances:
        cnt = 0
        for j, e in graph[i].iteritems():
            cnt += e
        counts.push(elm(i,cnt))

    while not counts.empty():
        popped = counts.pop()
        i = popped.key
        tot_bunnies = popped.value
        tmp  = dijkstra(graph,i)
        if tmp is None:
            continue
        # print graph
        # print tmp[0]
        # print tmp[1]
        best_guy, his_max = choose_best_guy(exits, tmp[0])
        while best_guy != -1:
            # print tmp[1]
            cpath = find_path(i, best_guy, tmp[1])
            # print "best guy", best_guy
            # print "current path", cpath
            # print factor
            count += his_max
            tot_bunnies -= his_max
            prev =None
            for p in cpath:
                if prev is not None:
                    graph[prev][p] -= his_max
                    if graph[prev][p] == 0:
                        del graph[prev][p]
                prev = p
            print graph
            if tot_bunnies == 0:
                break
            tmp  = dijkstra(graph,i)
            best_guy, his_max = choose_best_guy(exits, tmp[0])

        # print graph
    
    return count

def find_path(source,dest, ds):
    tmp = []
    # print "main dest",dest, ds
    while dest != source:
        tmp = [dest] + tmp
        dest = ds[dest]
    tmp = [dest] + tmp
    return tmp



def choose_best_guy(exits,ds):
    global infinity
    _max = -1
    maxIndex = None
    for i in exits:
        if ds[i] > _max and abs(ds[i]) != infinity:
            _max = ds[i]
            maxIndex = i
    if _max == -1 or _max == 0:
        return -1, None
    return maxIndex, _max
        




            

entrances = [0, 1]
exits = [6, 7]
path = [
  [0, 0, 2, 0, 0, 0, 0, 0],
  [0, 0, 3, 0, 0, 0, 0, 0],
  [0, 0, 0, 4, 4, 0, 0, 0],  # Room 0: Bunnies
  [0, 0, 0, 0, 0, 3, 1, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 0, 2, 0, 0],  # Room 2: Intermediate room
  [0, 0, 0, 0, 0, 0, 3, 2],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]
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
print answer(entrances,exits,path)