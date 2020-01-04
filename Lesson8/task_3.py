# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import collections

def createGraph(count_vertex):
    graph = collections.defaultdict(list)
    for i in range(count_vertex):
        for j in range(count_vertex):
            if j != i:
                graph[i].append(j)
    return graph



visited = []

def dfs(graph,node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)

g = createGraph(5)
print(g)
dfs(g, 2)
print(visited)




