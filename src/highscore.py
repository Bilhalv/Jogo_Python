def add_highscore(x):
    high = get_highscore()
    high.append(x)
    high.sort()
    with open("highscore.txt", "w") as file:
        for line in high:
            file.write(line + "\n")

def get_highscore():
    high = []
    with open("highscore.txt", "r") as file:
        for idx, line in enumerate(file.readlines()):
            line = line.rstrip()
            if "\n" in line:
                line = line[:-1]
            if idx < 5:
                high.append(line)
    high.sort()
    return high