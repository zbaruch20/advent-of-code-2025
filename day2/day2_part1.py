from constants import SAMPLE_INPUT, INPUT

def sum_invalid_ids_part_1(id_ranges: str) -> int:
    def validate(id: str) -> bool:
        mid = len(id) // 2
        return True if len(id) % 2 != 0 else id[:mid] != id[mid:]

    def parse_range(r: str):
        start, end = [int(x) for x in r.split('-')]
        return list(range(start, end + 1))

    return sum([id for id_range in [parse_range(r) for r in id_ranges.split(',')] for id in id_range if not validate(str(id))])

print(f"Sum of invalid IDs in sample input: {sum_invalid_ids_part_1(SAMPLE_INPUT)}")
print(f"Sum of invalid IDs in actual input: {sum_invalid_ids_part_1(INPUT)}")