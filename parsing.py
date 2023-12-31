

def parse_environment(file: str):
    grid = []
    robots = []
    goals = []
    with open(file) as f:
        for line in f.readlines():
            listed_line = line.split()
            if listed_line[0] == "R":
                robots.append((listed_line[1], listed_line[2]))
                goals.append((listed_line[3], listed_line[4]))
            else:
                grid.append(listed_line)
    
    return grid, robots, goals
                