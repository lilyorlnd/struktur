def shortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return []
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = shortestPath(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def findAllShortestPath(allpath, shorpath):
    ListShortest = []
    for path in allpath:
        if len(path) == len(shorpath):
           ListShortest.append(path)
    return ListShortest

def allPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if not node in path:
            newpath = allPath(graph, node, end, path)
            for newpaths in newpath:
                paths.append(newpaths)
    return paths

def findAllEdge(graph):
    ListEdge = []
    for i in graph.keys():
        if graph[i] != []:
            for j in graph[i]:
                temp = i+' => '+j
                ListEdge.append(temp)
    return ListEdge

def printGraph(path):
    for i in range(len(path)):
        print('Path', i+1, ':', path[i])

graphSembarang = {
    'A' : ['C', 'D'],
    'B' : ['C', 'E'],
    'C' : ['A', 'B', 'D', 'E'],
    'D' : ['C', 'E'],
    'E' : ['C', 'B'],
    'F' : []
}

edge = findAllEdge(graphSembarang)
printGraph(edge)

print()
semuaJalur = allPath(graphSembarang, 'A', 'E')
printGraph(semuaJalur)

print("\nRute terpendek dan Alternatifnya : ")
shortest = shortestPath(graphSembarang, 'A', 'E')
listShortest = findAllShortestPath(semuaJalur, shortest)
printGraph(listShortest) 