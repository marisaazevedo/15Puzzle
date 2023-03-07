from auxFunctions import Puzzle
from collections import deque
from queue import PriorityQueue
import sys

def misplacedTiles(puzzle, final):
    count = 0
    for i in range(16):
        if puzzle[i] != 0 and puzzle[i] != final[i]:
            count += 1
    return count

def manhattanDistance(puzzle, final):
    distance = 0
    for i in range(len(puzzle)):
        if puzzle[i] != 0:
            rowDist = abs(i//4 - (final.index(puzzle[i]))//4)
            colDist = abs(i%4 - (final.index(puzzle[i]))%4)
            distance += rowDist + colDist
    return distance


def dfs(root: list[int], final: list[int]) -> Puzzle:
    stack = deque()                         # criar uma pilha
    stack.append(Puzzle(root))              # adicionar a configuracao atual à pilha
    visited = set()                         # criar uma lista com apenas as configuracoes visitadas
    nodes = deque()

    while len(stack):
        puzzle = stack.pop()                # atribuir à variável puzzle o último elemento da pilha e retira-o da pilha
        nodes.append(puzzle)
        print(puzzle.array, len(visited))

        if tuple(puzzle.array) in visited:  # verificar se configuracao atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:           # verificar se a configuração atual é igual à configuracao final
            print(len(nodes))
            return puzzle.depth             # retorna o números passos para chegar da configuracao inicial à final

        if tuple(puzzle.left())not in visited:
            stack.append(Puzzle(puzzle.left(), depth = puzzle.depth + 1))
        if tuple(puzzle.right())not in visited:
            stack.append(Puzzle(puzzle.right(), depth = puzzle.depth + 1))
        if tuple(puzzle.up())not in visited:
            stack.append(Puzzle(puzzle.up(), depth = puzzle.depth + 1))
        if tuple(puzzle.down())not in visited:
            stack.append(Puzzle(puzzle.down(), depth = puzzle.depth + 1))

    raise Exception("Puzzle cannot be solved")

def bfs(root: list[int], final: list[int]):
    queue = deque()                             # criar uma fila
    queue.append(Puzzle(root))                  # adicionar a configuracao atual à fila
    visited = set()                             # criar uma lista com apenas as configuracoes visitadas
    mem = 0

    while len(queue):
        puzzle = queue.popleft()                # atribuir à variável puzzle o último elemento da pilha
        print(puzzle.array, len(visited))

        if tuple(puzzle.array) in visited:      # verificar se configuracao atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:               # verificar se a configuração atual é igual à configuracao final
            print(mem)
            return puzzle.depth                 # retorna o números passos para chegar da configuracao inicial à final

        if tuple(puzzle.left())not in visited:
            queue.append(Puzzle(puzzle.left(), depth = puzzle.depth + 1))
            mem +=1
        if tuple(puzzle.right())not in visited:
            queue.append(Puzzle(puzzle.right(), depth = puzzle.depth + 1))
            mem +=1
        if tuple(puzzle.up())not in visited:
            queue.append(Puzzle(puzzle.up(), depth = puzzle.depth + 1))
            mem +=1
        if tuple(puzzle.down())not in visited:
            queue.append(Puzzle(puzzle.down(), depth = puzzle.depth + 1))
            mem +=1

    raise Exception("Puzzle cannot be solved")

def idfs(root: list[int], final: list[int]) -> Puzzle:
    max_depth = 0
    while True:
        stack = deque()                             # criar uma pilha
        stack.append(Puzzle(root))                  # adicionar a configuracao atual à pilha
        visited = set()                             # criar uma lista com apenas as configuracoes visitadas

        while len(stack):
            puzzle = stack.pop()                    # atribuir à variável puzzle o último elemento da pilha e retira-o da pilha
            print(puzzle.array, len(visited))

            if tuple(puzzle.array) in visited:      # verificar se configuracao atual já foi visitada
                continue
            visited.add(tuple(puzzle.array))

            if puzzle.array == final:               # verificar se a configuração atual é igual à configuracao final
                return puzzle.depth                 # retorna o números passos para chegar da configuracao inicial à final

            if puzzle.depth < max_depth:
                if tuple(puzzle.left())not in visited:
                    stack.append(Puzzle(puzzle.left(), depth = puzzle.depth + 1))
                if tuple(puzzle.right())not in visited:
                    stack.append(Puzzle(puzzle.right(), depth = puzzle.depth + 1))
                if tuple(puzzle.up())not in visited:
                    stack.append(Puzzle(puzzle.up(), depth = puzzle.depth + 1))
                if tuple(puzzle.down())not in visited:
                    stack.append(Puzzle(puzzle.down(), depth = puzzle.depth + 1))

        max_depth += 1
        if max_depth > sys.maxsize:                 # numero arbitrario para limitar a profundidade
            break

    raise Exception("Puzzle cannot be solved")

def greedy_misplaced(root: list[int], final: list[int]) -> Puzzle:
    visited = set()
    q = PriorityQueue()
    q.put(Puzzle(root), misplacedTiles(root, final))

    while not q.empty():
        current = q.get()
        if current.array == final:
            return current.depth
        visited.add(tuple(current.array))

    if tuple(current.left())not in visited:
        q._put((Puzzle(current.left(), current.depth + 1)), (misplacedTiles(current.left(), final)))
    if tuple(current.right())not in visited:
        q._put((Puzzle(current.right(), current.depth + 1)), (misplacedTiles(current.right(), final)))
    if tuple(current.up())not in visited:
        q._put((Puzzle(current.up(), current.depth + 1), )(misplacedTiles(current.up(), final)))
    if tuple(current.down())not in visited:
        q._put((Puzzle(current.down(), current.depth + 1)), (misplacedTiles(current.down(), final)))

    raise Exception("Puzzle cannot be solved")

def greedy_manhattan(root: list[int], final: list[int]) -> Puzzle:
    visited = set()
    q = PriorityQueue()
    q.put(Puzzle(root), manhattanDistance(root, final))

    while not q.empty():
        current = q.get()
        if current.array == final:
            return current.depth
        visited.add(tuple(current.array))

    if tuple(current.left())not in visited:
        q.put(Puzzle(current.left(), current.depth + 1), (manhattanDistance(current.left(), final)))
    if tuple(current.right())not in visited:
        q.put(Puzzle(current.right(), current.depth + 1), (manhattanDistance(current.right(), final)))
    if tuple(current.up())not in visited:
        q.put(Puzzle(current.up(), current.depth + 1), (manhattanDistance(current.up(), final)))
    if tuple(current.down())not in visited:
        q.put(Puzzle(current.down(), current.depth + 1), (manhattanDistance(current.down(), final)))

    raise Exception("Puzzle cannot be solved")


def aStar_misplaced(i,f):
    return 0

def aStar_manhattan(i,f):
    return 0

# 1: GeneralSearchAlgorithm(QueueingFunction,configInicial,configFinal)
# 2: if thereIsNoSolution(configInicial,configFinal) then
# 3:    return “It is impossible to reach a solution”
# 4: end if
# 5: queue = configInicial
# 6: while queue not empty do
# 7:    node = removeFrontNodeFrom(queue)
# 8:    if node is solution then
# 9:        return Path to solution
# 10:   end if
# 11:   descendantList = MakeDescendants(node)
# 12:   insert(descendantList,queue,QueueingFunction)
# 13: end while
# 14: return “solution not found”
