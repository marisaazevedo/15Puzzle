from solvability import solvability
from auxFunctions import Puzzle
from heuristic import misplacedTiles, manhattanDistance
from board import board
from collections import deque
from queue import PriorityQueue
import sys
import time

def dfs(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if(not(solvability(root) == solvability(final))):
        print("There is no path between the final configuration and the initial configuration.")
        return 0

    print("Initial Configuration:")
    print(board(root))
    print("Final Configuration:")
    print(board(final))

    stack = deque()                         # criar uma pilha
    stack.append(Puzzle(root))              # adicionar a configuracao atual à pilha
    visited = set()                         # criar uma lista com apenas as configuracoes visitadas
    nodes = deque()
    mem = 0
    while len(stack):
        puzzle = stack.pop()                # atribuir à variável puzzle o último elemento da pilha e retira-o da pilha
        nodes.append(puzzle)

        if tuple(puzzle.array) in visited:  # verificar se configuracao atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:           # verificar se a configuração atual é igual à configuracao final
            end = time.time()
            print("Depth First Search: %d steps" %puzzle.depth)
            print("time = %f seconds" %(end - start))
            print("memory = %d" %mem)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:
            mem +=1
            if tuple(p) not in visited:
                stack.append(Puzzle(p, depth = puzzle.depth + 1))

    raise Exception("Puzzle cannot be solved")

def bfs(root: list[int], final: list[int]):
    start = time.time()
    if(not(solvability(root) == solvability(final))):
        print("There is no path between the final configuration and the initial configuration.")
        return 0

    print("Initial Configuration:")
    print(board(root))
    print("Final Configuration:")
    print(board(final))

    queue = deque()                             # criar uma fila
    queue.append(Puzzle(root))                  # adicionar a configuracao atual à fila
    visited = set()                             # criar uma lista com apenas as configuracoes visitadas
    mem = 0

    while len(queue):
        puzzle = queue.popleft()                # atribuir à variável puzzle o último elemento da pilha
        #print(puzzle.array, len(visited))

        if tuple(puzzle.array) in visited:      # verificar se configuracao atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:               # verificar se a configuração atual é igual à configuracao final
            end = time.time()
            print("Breadth First Search: %d steps" %puzzle.depth)
            print("time = %f seconds" %(end - start))
            print("memory = %d" %mem)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [right,up,down,left]:
            mem += 1
            if tuple(p) not in visited:
                queue.append(Puzzle(p, depth = puzzle.depth + 1))

    raise Exception("Puzzle cannot be solved")

def idfs(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if(not(solvability(root) == solvability(final))):
        print("There is no path between the final configuration and the initial configuration.")
        return 0

    print("Initial Configuration:")
    print(board(root))
    print("Final Configuration:")
    print(board(final))

    max_depth = 0
    while True:
        stack = deque()                             # criar uma pilha
        stack.append(Puzzle(root))                  # adicionar a configuracao atual à pilha
        visited = set()                             # criar uma lista com apenas as configuracoes visitadas
        mem = 0

        while len(stack):
            puzzle = stack.pop()                    # atribuir à variável puzzle o último elemento da pilha e retira-o da pilha
            #print(puzzle.array, len(visited))

            if tuple(puzzle.array) in visited:      # verificar se configuracao atual já foi visitada
                continue
            visited.add(tuple(puzzle.array))

            if puzzle.array == final:               # verificar se a configuração atual é igual à configuracao final
                end = time.time()
                print("Iterative Deepening Depth First Search: %d passos" %puzzle.depth)
                print("time = %f seconds" %(end - start))
                print("memory = %d" %mem)
                return 0

            if puzzle.depth < max_depth:
                left = puzzle.left()
                right = puzzle.right()
                up = puzzle.up()
                down = puzzle.down()

                for p in [down,up,right,left]:
                    mem += 1
                    if tuple(p) not in visited:
                        stack.append(Puzzle(p, depth = puzzle.depth + 1))
        max_depth += 1
        if max_depth > sys.maxsize:                 # numero arbitrario para limitar a profundidade
            break

    raise Exception("Puzzle cannot be solved")

def greedy_manhattan(root: list[int], final: list[int]) -> Puzzle:

    print("Initial Configuration:")
    print(board(root))
    print("Final Configuration:")
    print(board(final))

    start = time.time()

    if(not(solvability(root) == solvability(final))):
        print("There is no path between the final configuration and the initial configuration.")
        return 0

    visited = set()
    q = PriorityQueue()
    q.put((manhattanDistance(root, final),Puzzle(root)))
    mem = 0
    while not q.empty():
        _, puzzle = q.get()

        if puzzle.array == final:
            end = time.time()
            print("Greedy Manhattan: %d steps" %puzzle.depth)
            print("time = %f segundos" %(end - start))
            print("memory = %d" %mem)
            return 0
        visited.add(tuple(puzzle.array))

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:
            mem += 1
            if tuple(p) not in visited:
                q.put((manhattanDistance(p, final), Puzzle(p, puzzle.depth + 1)))

    raise Exception("Puzzle cannot be solved")

def greedy_misplaced(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if(not(solvability(root) == solvability(final))):
        print("There is no path between the final configuration and the initial configuration.")
        return 0

    print("Initial Configuration:")
    print(board(root))
    print("Final Configuration:")
    print(board(final))

    h = misplacedTiles(root, final)             # calcula a heurística inicial, ou seja, o numero de pecas fora do lugar de acordo com a configuração final
    pq = PriorityQueue()                        # cria uma fila de prioridade vazia
    pq.put((h,Puzzle(root)))                    # adiciona a configuração inicial à fila com a heurística calculada
    visited = set()                             # cria uma lista com apenas as configurações visitadas
    nodes = deque()                             # cria
    mem = 0

    while not pq.empty():
        _, puzzle = pq.get()                    # extrai a configuração com menor heurística da fila
        nodes.append(puzzle)

        if tuple(puzzle.array) in visited:      # verifica se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:               # verifica se a configuração atual é igual à configuração final
            end = time.time()
            print("Greedy Misplaced: %d steps" %puzzle.depth)
            print("time = %f seconds" %(end - start))
            print("memory = %d" %mem)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:
            mem += 1
            if tuple(p) not in visited:
                pq.put((misplacedTiles(p, final), Puzzle(p,depth=puzzle.depth +1)))

    raise Exception("Puzzle cannot be solved")

def aStar_misplaced(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if(not(solvability(root) == solvability(final))):
        print("There is no path between the final configuration and the initial configuration.")
        return 0

    print("Initial Configuration:")
    print(board(root))
    print("Final Configuration:")
    print(board(final))

    pq = PriorityQueue()
    pq.put((0 + misplacedTiles(root, final), Puzzle(root)))            # adicionar a configuracao atual à fila, com a prioridade inicial
    visited = set()                                                    # criar uma lista com apenas as configuracoes visitadas
    nodes = deque()
    mem = 0

    while not pq.empty():
        _, puzzle = pq.get()                                           # obter o próximo estado na fila

        if tuple(puzzle.array) in visited:                             # verificar se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:                                      # verificar se a configuração atual é igual à configuração final
            end = time.time()
            print("A* Misplaced: %d steps" %puzzle.depth)
            print("time = %f seconds" %(end - start))
            print("memory = %d" %mem)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down, up, right, left]:
            mem += 1
            if tuple(p) not in visited:
                priority = puzzle.depth + 1 + misplacedTiles(p, final)
                pq.put((priority, Puzzle(p, depth=puzzle.depth + 1)))
                nodes.append(puzzle)

    raise Exception("Puzzle cannot be solved")


def aStar_manhattan(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if(not(solvability(root) == solvability(final))):
        print("There is no path between the final configuration and the initial configuration.")
        return 0

    print("Initial Configuration:")
    print(board(root))
    print("Final Configuration:")
    print(board(final))

    pq = PriorityQueue()
    pq.put((0 + manhattanDistance(root, final), Puzzle(root)))              # adicionar a configuracao atual à fila, com a prioridade inicial
    visited = set()                                                         # criar uma lista com apenas as configuracoes visitadas
    nodes = deque()
    mem = 0

    while not pq.empty():
        _, puzzle = pq.get()                                                # obter o próximo estado na fila

        if tuple(puzzle.array) in visited:                                  # verificar se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:                                          # verificar se a configuração atual é igual à configuração final
            end = time.time()
            print("A* Manhattan: %d steps" %puzzle.depth)
            print("time = %f seconds" %(end - start))
            print("memory = %d" %mem)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down, up, right, left]:
            mem += 1
            if tuple(p) not in visited:
                priority = puzzle.depth + 1 + manhattanDistance(p, final)
                pq.put((priority, Puzzle(p, depth=puzzle.depth + 1)))
                nodes.append(puzzle)

    raise Exception("Puzzle cannot be solved")
