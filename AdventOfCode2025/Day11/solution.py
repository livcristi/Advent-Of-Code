# from collections import defaultdict
# from functools import lru_cache
#
# graph = defaultdict(list)
#
# with open("input.txt") as f_inp:
#     for line in f_inp:
#         start_node, other_nodes = line.split(":")
#         start_node = start_node.strip()
#         other_nodes = [node.strip() for node in other_nodes.split(" ") if node.strip()]
#         graph[start_node] = other_nodes
#
#
# def bfs(start_node, end_node):
#     num_paths = defaultdict(int)
#     num_paths[start_node] = 1
#     node_queue = list()
#     node_queue.append(start_node)
#     visited = set()
#
#     while node_queue:
#         current_node = node_queue.pop(0)
#
#         if current_node in visited:
#             continue
#
#         visited.add(current_node)
#         for next_node in graph[current_node]:
#             if next_node not in visited:
#                 num_paths[next_node] += num_paths[current_node]
#                 node_queue.append(next_node)
#
#     return num_paths[end_node]
#
#
# @lru_cache(None)
# def dfs(node, seen_dac, seen_fft):
#     if node == "out":
#         return 1 if (seen_dac and seen_fft) else 0
#
#     paths = 0
#     for nxt in graph[node]:
#         paths += dfs(
#             nxt,
#             seen_dac or (nxt == "dac"),
#             seen_fft or (nxt == "fft"),
#         )
#     return paths
#
#
# total = bfs("you", "out")
# total_2 = dfs("svr", False, False)
#
# print(total, total_2)

from collections import defaultdict
from functools import lru_cache
from typing import List, Dict, Set

graph: Dict[str, List[str]] = {
    parts[0].strip(): [n.strip() for n in parts[1].split(" ") if n.strip()]
    for line in open("input.txt")
    if (parts := line.split(":"))
}

# Simple bfs to count the number of paths between two nodes
def bfs(start_node: str, end_node: str) -> int:
    num_paths: Dict[str, int] = defaultdict(int)
    num_paths[start_node] = 1
    node_queue: List[str] = [start_node]
    visited: Set[str] = set()

    while node_queue:
        current_node: str = node_queue.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)
        for next_node in graph.get(current_node, []):
            if next_node not in visited:
                # Accumulate path counts to the next frontier
                num_paths[next_node] += num_paths[current_node]
                node_queue.append(next_node)

    return num_paths[end_node]


# Specialized dfs for the second case, where we also keep track if we saw the intermediary nodes along the path
@lru_cache(None)
def dfs(node: str, seen_dac: bool, seen_fft: bool) -> int:
    # We return 1 only if we also saw dac and fft along the traversed path
    if node == "out":
        return 1 if (seen_dac and seen_fft) else 0

    # Otherwise, we continue the path with the neighbours
    paths: int = 0
    for nxt in graph.get(node, []):
        paths += dfs(nxt, seen_dac or (nxt == "dac"), seen_fft or (nxt == "fft"),)
    return paths


total: int = bfs("you", "out")
total_2: int = dfs("svr", False, False)

print(total, total_2)
