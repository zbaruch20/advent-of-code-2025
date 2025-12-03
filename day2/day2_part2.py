from constants import SAMPLE_INPUT, INPUT

def sum_invalid_ids_part_2(id_ranges: str) -> int:
    def validate(id: str) -> bool:
        def validate_chunk(chunk: str) -> bool:
            if len(id) == 1 or len(id) % len(chunk) != 0:
                return True
            
            for i in range(len(chunk), len(id), len(chunk)):
                if id[i:i+len(chunk)] != chunk:
                    return True
            return False

        return not (False in [validate_chunk(chunk) for chunk in [id[0:i+1] for i in range(0, len(id) // 2)]])

    def parse_range(r: str):
        start, end = [int(x) for x in r.split('-')]
        return list(range(start, end + 1))

    return sum([id for id_range in [parse_range(r) for r in id_ranges.split(',')] for id in id_range if not validate(str(id))])

print(f"Sum of invalid IDs in sample input: {sum_invalid_ids_part_2(SAMPLE_INPUT)}")
print(f"Sum of invalid IDs in actual input: {sum_invalid_ids_part_2(INPUT)}")