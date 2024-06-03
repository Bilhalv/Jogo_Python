def add_highscore(x:tuple[str, int]):
    high = get_highscore()
    high.append(x)
    high.sort(key=lambda x: x[1])
    with open("highscore.txt", "w") as file:
        for line in high:
            file.write(f"{line[0]}: {line[1]}\n")

def get_highscore() -> list[tuple[str, int]]:
    high = []
    with open("highscore.txt", "r") as file:
        for idx, line in enumerate(file.readlines()):
            line = line.rstrip()
            if "\n" in line:
                line = line[:-1]
            final = line.split(": ")
            high.append((final[0], int(final[1])))
    high.sort(key=lambda x: x[1], reverse=True)
    return high[:5]