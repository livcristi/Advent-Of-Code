import heapq
import math
from typing import List, Tuple, Dict, Set

junction_boxes: List[Tuple[int, int, int]] = [
    tuple(map(int, line.split(","))) for line in open("input.txt")
]


def calculate_distance(p1: Tuple[int, int, int], p2: Tuple[int, int, int]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


edges: List[Tuple[Tuple[int, int, int], Tuple[int, int, int], float]] = []
num_boxes = len(junction_boxes)

for index in range(num_boxes):
    for index_2 in range(index + 1, num_boxes):
        box_1, box_2 = junction_boxes[index], junction_boxes[index_2]
        edges.append((box_1, box_2, calculate_distance(box_1, box_2)))

# We will keep adding edges from shortest to longest, so we first need to sort them
edges.sort(key=lambda x: x[2])

# We will also need to implement the Disjoint Set Union algorithm to keep connecting the edges in a Kruskal fashion
class DSU:
    def __init__(self, items: List[Tuple[int, int, int]]) -> None:
        self.parent: Dict[Tuple[int, int, int], Tuple[int, int, int]] = {
            item: item for item in items
        }
        self.sizes: Dict[Tuple[int, int, int], int] = {item: 1 for item in items}

    def find(self, item: Tuple[int, int, int]) -> Tuple[int, int, int]:
        root: Tuple[int, int, int] = item
        while self.parent[root] != root:
            root = self.parent[root]

        while item != root:
            next_item = self.parent[item]
            self.parent[item] = root
            item = next_item

        return root

    def union(self, item: Tuple[int, int, int], item_2: Tuple[int, int, int]) -> None:
        root1: Tuple[int, int, int] = self.find(item)
        root2: Tuple[int, int, int] = self.find(item_2)

        if root1 == root2:
            return

        smaller, larger = (
            (root1, root2) if self.sizes[root1] < self.sizes[root2] else (root2, root1)
        )
        self.sizes[larger] += self.sizes[smaller]
        self.parent[smaller] = larger
        del self.sizes[smaller]


def join_boxes(connections_limit: int) -> int:
    dsu: DSU = DSU(junction_boxes)

    for index in range(connections_limit):
        box_1, box_2, _ = edges[index]
        dsu.union(box_1, box_2)

    # Get the sizes for the connected components and return the product for the top 3
    top3 = heapq.nlargest(3, dsu.sizes.values())

    return top3[0] * top3[1] * top3[2]


def join_all_boxes() -> int:
    dsu: DSU = DSU(junction_boxes)

    for box_1, box_2, _ in edges:
        dsu.union(box_1, box_2)

        # If we are left with only one component, we return the answer based on the last boxes
        if len(dsu.sizes) == 1:
            return box_1[0] * box_2[0]

    return 0


print(join_boxes(1000), join_all_boxes())
