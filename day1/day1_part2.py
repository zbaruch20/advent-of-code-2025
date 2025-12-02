def update_position(old_pos: int, dir: str, rotation: int) -> int | int:
    zero_touches = rotation // 100 # step 1: complete rotations

    new_pos = (old_pos + rotation % 100) if dir == "R" else (old_pos - rotation % 100)
    if old_pos != 0 and (new_pos <= 0 or new_pos >= 100):
        zero_touches += 1

    return new_pos % 100, zero_touches

def __main__() -> None:
    password = 0
    position = 50
    
    with open("./input.txt") as file:
        for line in file.readlines():
            dir = line[0]
            rotation = int(line[1:])
            position, zero_touches = update_position(position, dir, rotation)
            password += zero_touches
    
    print(f"Password: {password}")

if __name__ == "__main__":
    __main__()