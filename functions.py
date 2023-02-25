from auxFunctions import Puzzle

from collections import deque

def dfs(root: list[int], final: list[int]) -> Puzzle:
    stack = deque()
    stack.append(Puzzle(root))
    visited = set()

    while len(stack):
        puzzle = stack.pop()
        print(puzzle.array, len(visited))

        if tuple(puzzle.array) in visited:
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:
            return puzzle

        stack.append(Puzzle(puzzle.left(), depth = puzzle.depth + 1))
        stack.append(Puzzle(puzzle.right(), depth = puzzle.depth + 1))
        stack.append(Puzzle(puzzle.up(), depth = puzzle.depth + 1))
        stack.append(Puzzle(puzzle.down(), depth = puzzle.depth + 1))

    raise Exception("Puzzle cannot be solved")

def bfs(i,f):
    # queue = deque()
    # queue.append(i)
    # while(len(queue) > 0):
    #     node = queue.popleft()
    #     if node
    return 0

def ids(i,f):
    return 0

def a(i,f):
    return 0

def g(i,f):
    return 0

##1: GeneralSearchAlgorithm(QueueingFunction,configInicial,configFinal)
##2: if thereIsNoSolution(configInicial,configFinal) then
##3:    return “It is impossible to reach a solution”
##4: end if
##5: queue = configInicial
##6: while queue not empty do
##7:    node = removeFrontNodeFrom(queue)
##8:    if node is solution then
##9:        return Path to solution
##10:   end if
##11:   descendantList = MakeDescendants(node)
##12:   insert(descendantList,queue,QueueingFunction)
##13: end while
##14: return “solution not found”
