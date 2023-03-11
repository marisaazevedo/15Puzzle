def manhattanDistance(puzzle, final):
    distance = 0
    for i in range(len(puzzle)):
        if puzzle[i] != 0:
            rowDist = abs(i // 4 - final.index(puzzle[i]) // 4)
            colDist = abs(i % 4 - final.index(puzzle[i]) % 4)
            distance += rowDist + colDist
    return distance

def misplacedTiles(puzzle, final):
    count = 0
    for i in range(len(puzzle)):
        if puzzle[i] != final[i]:
            count += 1
    return count
