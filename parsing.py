

def parse_environment(file: str) -> (list[list], dict(), dict()):
    grid = []
    robots = dict()
    goals = dict()
    with open(file) as f:
        read_grid = False
        for line in f.readlines():
            listed_line = line.split()
            if listed_line:
                if read_grid:
                    grid.append(listed_line)
                else:
                    robots[listed_line[0]] = (int(listed_line[1]), int(listed_line[2]))
                    goals[listed_line[0]] = (int(listed_line[3]), int(listed_line[4]))

            else:
                read_grid = True
    
    return grid, robots, goals
                