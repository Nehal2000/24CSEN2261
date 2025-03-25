def prim_mst(graph, start):
    mst = []
    in_mst = {start}
    edges = graph[start]
    total_weight = 0

    while len(in_mst) < len(graph):
        min_edge = None
        for u in in_mst:
            for v, weight in graph[u]:
                if v not in in_mst and (min_edge is None or weight < min_edge[2]):
                    min_edge = (u, v, weight)

        mst.append(min_edge)
        total_weight += min_edge[2]
        in_mst.add(min_edge[1])

    return total_weight, mst

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

total_weight, mst = prim_mst(graph, 'A')
print("Total weight of MST:", total_weight)
print("Edges in MST:", mst)
