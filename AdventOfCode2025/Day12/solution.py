from typing import List, Tuple

with open("input.txt") as f_inp:
    raw_data: List[str] = f_inp.read().strip().split("\n\n")
    shapes_raw: List[str] = raw_data[:-1]
    regions_raw: str = raw_data[-1]

    def process_shape(shape_data: str) -> List[List[int]]:
        index, matrix = shape_data.split(":")

        matrix_int: List[List[int]] = [
            [int(char == "#") for char in row.strip()]
            for row in matrix.strip().split("\n")
        ]

        return matrix_int

    def process_region(region_data: str) -> Tuple[List[int], List[int]]:
        sizes, counts = region_data.split(":")
        sizes_val: List[int] = [int(val) for val in sizes.split("x")]
        counts_val: List[int] = [int(val) for val in counts.split(" ") if val.strip()]

        return sizes_val, counts_val

    shapes: List[List[List[int]]] = [process_shape(s) for s in shapes_raw]
    regions: List[Tuple[List[int], List[int]]] = [
        process_region(r) for r in regions_raw.split("\n") if r.strip()
    ]


def can_fit(
    shapes_data: List[List[List[int]]], sizes: List[int], shapes_count: List[int]
) -> bool:
    # Simple heuristic
    def get_shape_area(shape_data: List[List[int]]) -> int:
        return sum(sum(row) for row in shape_data)

    shapes_area: List[int] = [get_shape_area(shape) for shape in shapes_data]
    total_used: int = sum(
        area * count for area, count in zip(shapes_area, shapes_count)
    )

    return total_used <= sizes[0] * sizes[1]


total: int = sum(1 for region in regions if can_fit(shapes, region[0], region[1]))

print(total)
