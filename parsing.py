

def parse_environment(file: str):
    grid = []
    robots = {}
    goals = {}
    with open(file) as f:
        read_grid = False
        for line in f.readlines():
            listed_line = line.split()
            if listed_line:
                if read_grid:
                    grid.append(listed_line)
                else:
                    robots[listed_line[0]] = (listed_line[1], listed_line[2])
                    goals[listed_line[0]] = (listed_line[3], listed_line[4])

            else:
                read_grid = True
    
    return grid, robots, goals
                