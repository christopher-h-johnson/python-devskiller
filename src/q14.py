from typing import List
import networkx as nx
import matplotlib.pyplot as plt


def solve(input: str) -> List[List[int]]:
    lines = input.splitlines()
    data = lines[1:]

    nodes = []
    edges = []
    for t in data:
        x = int(t.split(' ')[0])
        y = int(t.split(' ')[1])
        nodes.append(x)
        edges.append([x, y])
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # convert graph to dict
    graph = dict()
    for n in G.nodes:
        neighbors = G.neighbors(n)
        nlist = []
        for neigh in neighbors:
            nlist.append(neigh)
            graph.update({n: nlist})
    print(graph)
    # adjacency logic
    blacks = []
    whites = []
    HEAD = 1
    for (k, v) in graph.items():
        if k == HEAD:
            whites.append(k)
            for i in v:
                if i not in blacks:
                    blacks.append(i)
                    for b in blacks:
                        b_neighbors = graph.get(b)
                        for n in b_neighbors:
                            if n not in whites:
                                whites.append(n)
                            else:
                                for w in whites:
                                    w_neighbors = graph.get(w)
                                    for nw in w_neighbors:
                                        if nw not in blacks:
                                            blacks.append(nw)

    # print graph for reference
    options = {
        "font_size": 36,
        "node_size": 2000,
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    color_map = []
    for node in G:
        if node in whites:
            color_map.append('blue')
        else:
            color_map.append('green')
    nx.draw_networkx(G, node_color=color_map, **options)

    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()

    return sorted([sorted(whites), sorted(blacks)])
