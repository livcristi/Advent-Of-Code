import networkx as nx

# filename = "test-data.txt"


filename = "data.txt"


def make_graph(matrix_data):
    maze = nx.DiGraph()
    directions = [1, -1j, -1, 1j]
    start_node, end_node = None, None

    for row_index in range(len(matrix_data)):
        for col_index in range(len(matrix_data[row_index])):
            if matrix_data[row_index][col_index] == "#":
                continue
            complex_position = col_index + row_index * 1j
            if matrix_data[row_index][col_index] == "S":
                start_node = (complex_position, 1)
            if matrix_data[row_index][col_index] == "E":
                end_node = complex_position
            for direction in directions:
                maze.add_node((complex_position, direction))

    for node_position, node_direction in maze.nodes:
        if maze.has_node((node_position + node_direction, node_direction)):
            maze.add_edge(
                (node_position, node_direction),
                (node_position + node_direction, node_direction),
                weight=1,
            )
        for rotation in 1j, -1j:
            maze.add_edge(
                (node_position, node_direction),
                (node_position, node_direction * rotation),
                weight=1000,
            )

    for direction in directions:
        maze.add_edge((end_node, direction), "end", weight=0)

    return start_node, maze


def get_shortest_path(start_node, maze):
    result = nx.shortest_path_length(maze, source=start_node, target="end", weight="weight")
    return result


def get_shortest_paths_nodes(start_node, maze):
    all_paths = nx.all_shortest_paths(maze, source=start_node, target="end", weight="weight")
    return len({node for path in all_paths for node, _ in path[:-1]})


with open(filename, "r") as f_inp:
    raw_matrix_data = [list(char for char in line.strip()) for line in f_inp.read().splitlines()]
    start_node, maze = make_graph(raw_matrix_data)
    print(get_shortest_path(start_node, maze))
    print(get_shortest_paths_nodes(start_node, maze))
