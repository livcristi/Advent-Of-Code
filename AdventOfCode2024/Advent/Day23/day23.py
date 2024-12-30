import networkx as nx

# filename = "test-data.txt"


filename = "data.txt"


def count_cliques_3(connections):
    graph = nx.Graph()
    counter = 0
    for connection in connections:
        graph.add_edge(connection[0], connection[1])
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) == 3:
            for node in clique:
                if node.startswith("t"):
                    counter += 1
                    break
    return counter


def find_password(connections):
    graph = nx.Graph()
    for connection in connections:
        graph.add_edge(connection[0], connection[1])
    largest_size = 0
    best_clique = []
    for clique in nx.find_cliques(graph):
        if len(clique) > largest_size:
            largest_size = len(clique)
            best_clique = clique
    return ','.join(sorted(best_clique))


with open(filename, "r") as f_inp:
    connections_data = [tuple(line.strip().split('-')) for line in f_inp.readlines()]
    print(count_cliques_3(connections_data))
    print(find_password(connections_data))
