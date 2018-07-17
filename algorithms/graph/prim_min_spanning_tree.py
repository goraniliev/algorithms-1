'''
Implementation of Prim's Minimum Spanning Tree (for undirected graph): https://en.wikipedia.org/wiki/Prim%27s_algorithm

A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected,
edge-weighted (un)directed graph that connects all the vertices together, without any cycles and with
the minimum possible total edge weight.

Prim's algorithm starts with one node from the graph. After that it adds the closest node connected to that node.
In the next step it adds the node closest to one of the 2 already added nodes
(of course, only nodes which aren't already included are being considered). This continues until all nodes
are added.
'''


class Graph:
    def __init__(self, N):
        '''
        adj is a dict which contains the distance between adjacent elements in the graph
        :param N: number of nodes in the graph
        '''
        self.N = N
        self.adj = {}
        for i in range(1, N + 1):
            self.adj[i] = dict()

    def add_edge(self, from_, to, weight):
        '''
        Adding the weight twice because the graph is undirected.
        '''
        self.adj[from_][to] = weight
        self.adj[to][from_] = weight

    def prim(self, start):
        min_span_tree = Graph(self.N)

        included_nodes = {start}

        while len(included_nodes) < self.N:
            closest_node = 0
            closest_weight = None
            from_node = 0
            for node in included_nodes:
                for next_node, weight in self.adj[node].items():
                    if next_node not in included_nodes and (closest_weight is None or weight < closest_weight):
                        from_node = node
                        closest_node = next_node
                        closest_weight = weight
            included_nodes.add(closest_node)
            min_span_tree.add_edge(from_node, closest_node, closest_weight)

        return min_span_tree

    def get_edges(self):
        edges = list()
        for node, neighbors in self.adj.items():
            for neighbor in neighbors:
                if node < neighbor:
                    edges.append((node, neighbor))
        return edges


if __name__ == '__main__':
    '''
    Example input:
    1st line contains number of nodes N and number of edges E
    Each of the following E lines contains 3 values: the 2 nodes of the i-th edge, followed by the weight of that edge.
    The last line contains 1 integer, the starting node of the Prim algorithm.
    3 3
    2 1 20
    3 1 20
    2 3 100
    1
    '''
    (nodes_in_graph, edges_in_graph) = map(int, input().split())
    g = Graph(nodes_in_graph)
    for i in range(edges_in_graph):
        f, t, w = map(int, input().split())
        g.add_edge(f, t, w)
    start = int(input())
    prim = g.prim(start)
    print('The minimum spanning tree contains the following edges:')
    for edge in prim.get_edges():
        print(edge)

    s = 0
    for neigh in prim.adj.values():
        s += sum(neigh.values())
    print(f'The sum of all nodes in the minimum spanning tree is {s // 2}')
