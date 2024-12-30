filename = "test-data.txt"


# filename = "data.txt"


def create_disk_fragmentation(disk_data: str) -> list[int]:
    fragmentation = []
    is_free = False
    disk_index = 0
    frag_index = 0
    while disk_index < len(disk_data):
        if is_free:
            fragmentation.extend([None] * int(disk_data[disk_index]))
        else:
            fragmentation.extend([frag_index] * int(disk_data[disk_index]))
            frag_index += 1
        is_free = not is_free
        disk_index += 1
    return fragmentation


def defragment_fragmentation(fragmentation: list[int]) -> list[int]:
    start_index = 0
    end_index = len(fragmentation) - 1
    while start_index < end_index:
        if fragmentation[start_index] is None:
            while end_index > start_index and fragmentation[end_index] is None:
                end_index -= 1
            if start_index < end_index:
                fragmentation[start_index], fragmentation[end_index] = (
                    fragmentation[end_index],
                    fragmentation[start_index],
                )
        start_index += 1
    return fragmentation


def get_disk_checksum(disk_data: str) -> int:
    disk_fragmentation = create_disk_fragmentation(disk_data)
    defragmented_disk = defragment_fragmentation(disk_fragmentation)
    total = 0
    for index, value in enumerate(defragmented_disk):
        if value is not None:
            total += index * value
    return total


def move_file_index(fragmentation: list[int], file_index: int) -> list[int]:
    file_length = fragmentation.count(file_index)
    file_start = fragmentation.index(file_index)
    frag_index = 0
    while frag_index < len(fragmentation) and frag_index < file_start:
        if fragmentation[frag_index] is None:
            free_count = 1
            end_free = frag_index
            while (
                end_free + 1 < len(fragmentation)
                and fragmentation[end_free + 1] is None
            ):
                end_free += 1
                free_count += 1
            if free_count >= file_length:
                for index in range(file_start, file_start + file_length):
                    fragmentation[index] = None
                for index in range(frag_index, frag_index + file_length):
                    fragmentation[index] = file_index
                return fragmentation
            frag_index = end_free + 1
        else:
            frag_index += 1
    return fragmentation


def get_efficient_disk_defragmentation(fragmentation: list[int]) -> list[int]:
    for file_index in range(fragmentation[-1], 0, -1):
        move_file_index(fragmentation, file_index)
    return fragmentation


def get_efficient_disk_checksum(disk_data: str) -> int:
    disk_fragmentation = create_disk_fragmentation(disk_data)
    # print(disk_fragmentation)
    defragmented_disk = get_efficient_disk_defragmentation(disk_fragmentation)
    # print(defragmented_disk)
    total = 0
    for index, value in enumerate(defragmented_disk):
        if value is not None:
            total += index * value
    return total


with open(filename, "r") as f_inp:
    data = f_inp.read().strip()
    print(get_disk_checksum(data))
    print(get_efficient_disk_checksum(data))
