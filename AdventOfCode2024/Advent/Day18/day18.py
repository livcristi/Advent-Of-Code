import networkx as nx

# filename = "test-data.txt"


filename = "data.txt"


def make_graph(positions_data, max_width, max_height):
    memory = nx.DiGraph()
    directions = [1, -1j, -1, 1j]
    for x_value in range(max_width + 1):
        for y_value in range(max_height + 1):
            if (x_value, y_value) not in positions_data:
                memory.add_node(y_value + x_value * 1j)
    for x_value in range(max_width + 1):
        for y_value in range(max_height + 1):
            if (x_value, y_value) not in positions_data:
                for direction in directions:
                    if y_value + x_value * 1j + direction in memory.nodes:
                        memory.add_edge(y_value + x_value * 1j, y_value + x_value * 1j + direction, weight=1)
    return memory


def find_shortest_route(positions_data, max_width, max_height):
    memory = make_graph(positions_data, max_width, max_height)
    return nx.shortest_path_length(memory, source=0, target=max_height + max_width * 1j, weight="weight")


def find_faulty_pixel(positions_data, max_width, max_height):
    left, right = 0, len(positions_data) - 1
    faulty_pixel = None

    while left <= right:
        mid = (left + right) // 2
        try:
            find_shortest_route(positions_data[:mid + 1], max_width, max_height)
            left = mid + 1  # Continue to the right
        except nx.NetworkXNoPath:
            faulty_pixel = positions_data[mid]
            right = mid - 1  # Narrow down to the left

    return faulty_pixel


with open(filename, "r") as f_inp:
    all_positions = [tuple(map(int, line.split(","))) for line in f_inp.readlines()]
    # print(find_shortest_route(all_positions[:12], 6, 6))
    print(find_shortest_route(all_positions[:1024], 70, 70))
    # print(find_faulty_pixel(all_positions, 6, 6))
    print(find_faulty_pixel(all_positions, 70, 70))
