def update_position(old_pos: int, dir: str, rotation: int) -> int:
    new_pos = (old_pos + rotation) if dir == "R" else (old_pos - rotation)
    return new_pos % 100

def __main__() -> None:
    password = 0
    position = 50
    
    with open("./input.txt") as file:
        for line in file.readlines():
            dir = line[0]
            rotation = int(line[1:])
            position = update_position(position, dir, rotation)

            if position == 0:
                password += 1
    
    print(f"Password: {password}")

if __name__ == "__main__":
    __main__()