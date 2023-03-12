from solvability import solvability
from auxFunctions import Puzzle
from heuristic import misplacedTiles, manhattanDistance
from board import board
from collections import deque
from queue import PriorityQueue
import sys
import time
import copy

def dfs(root: list[int], final: list[int]) -> Puzzle:

    start = time.time()

    if solvability(root) != solvability(final):
        print("There is no path between the initial configuration and the final configuration.")
        return 0

    print("Initial Configuration:")
    board(root)
    print("Final Configuration:")
    board(final)

    stack = deque()                         # criar uma pilha
    stack.append(Puzzle(root))              # adicionar a configuracao atual à pilha
    visited = set()                         # criar uma lista com apenas as configuracoes visitadas
    mem = 0

    while len(stack):
        puzzle = stack.pop()                # atribuir à variável puzzle o último elemento da pilha e retira-o da pilha

        if tuple(puzzle.array) in visited:  # verificar se configuracao atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:           # verificar se a configuração atual é igual à configuracao final
            end = time.time()

            print("Depth First Search: %d steps" % puzzle.depth)
            print("time = %f seconds" % (end - start))
            print("memory = %d" % mem)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:
            if p is None:
                continue
            mem += 1
            if tuple(p.array) not in visited:
                stack.append(p)

    raise Exception("Puzzle cannot be solved")

def bfs(root: list[int], final: list[int]):
    start = time.time()

    if solvability(root) != solvability(final):
        print("There is no path between the initial configuration and the final configuration.")
        return 0

    print("Initial Configuration:")
    board(root)
    print("Final Configuration:")
    board(final)

    queue = deque()                             # criar uma fila
    queue.append(Puzzle(root))                  # adicionar a configuracao atual à fila
    visited = set()                             # criar uma lista com apenas as configuracoes visitadas
    mem = 0

    while len(queue):
        puzzle = queue.popleft()                # atribuir à variável puzzle o último elemento da pilha

        if tuple(puzzle.array) in visited:      # verificar se configuracao atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:               # verificar se a configuração atual é igual à configuracao final
            end = time.time()

            print("Breadth First Search: %d steps" % puzzle.depth)
            print("time = %f seconds" % (end - start))
            print("memory = %d" % mem)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [right,up,down,left]:
            if p is None:
                continue
            mem += 1
            if tuple(p.array) not in visited:
                queue.append(p)

    raise Exception("Puzzle cannot be solved")

def idfs(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if solvability(root) != solvability(final):
        print("There is no path between the initial configuration and the final configuration.")
        return 0

    print("Initial Configuration:")
    board(root)
    print("Final Configuration:")
    board(final)

    max_depth = 0

    while True:
        stack = deque()                             # criar uma pilha
        stack.append(Puzzle(root))                  # adicionar a configuracao atual à pilha
        visited = set()                             # criar uma lista com apenas as configuracoes visitadas
        mem = 0

        while len(stack):
            puzzle = stack.pop()                    # atribuir à variável puzzle o último elemento da pilha e retira-o da pilha

            if tuple(puzzle.array) in visited:      # verificar se configuracao atual já foi visitada
                continue
            visited.add(tuple(puzzle.array))

            if puzzle.array == final:               # verificar se a configuração atual é igual à configuracao final
                end = time.time()

                print("Iterative Deepening Depth First Search: %d passos" % puzzle.depth)
                print("time = %f seconds" % (end - start))
                print("memory = %d" % mem)
                return 0

            if puzzle.depth < max_depth:
                left = puzzle.left()
                right = puzzle.right()
                up = puzzle.up()
                down = puzzle.down()

                for p in [right,up,down,left]:
                    if p is None:
                        continue
                    mem += 1
                    if tuple(p.array) not in visited:
                        stack.append(p)

        max_depth += 1
        if max_depth > sys.maxsize:                 # numero arbitrario para limitar a profundidade
            break

    raise Exception("Puzzle cannot be solved")

def greedy_manhattan(root: list[int], final: list[int]) -> Puzzle:

    print("Initial Configuration:")
    board(root)
    print("Final Configuration:")
    board(final)

    start = time.time()

    if solvability(root) != solvability(final):
        print("There is no path between the initial configuration and the final configuration.")
        return 0

    visited = set()
    q = PriorityQueue()
    q.put((manhattanDistance(root, final),Puzzle(root)))
    mem = 0

    while not q.empty():
        _, puzzle = q.get()

        if puzzle.array == final:
            end = time.time()

            print("Greedy Manhattan: %d steps" % puzzle.depth)
            print("time = %f segundos" % (end - start))
            print("memory = %d" % mem)
            print("cost = %d" % puzzle.cost)            
            return 0
        visited.add(tuple(puzzle.array))

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [right,up,down,left]:
            if p is None:
                continue
            mem += 1
            if tuple(p.array) not in visited:
                p.cost = puzzle.cost + manhattanDistance(p.array, final)
                q.put((manhattanDistance(p.array, final),p))

    raise Exception("Puzzle cannot be solved")

def greedy_misplaced(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if solvability(root) != solvability(final):
        print("There is no path between the initial configuration and the final configuration.")
        return 0

    print("Initial Configuration:")
    board(root)
    print("Final Configuration:")
    board(final)

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

            print("Greedy Misplaced: %d steps" % puzzle.depth)
            print("time = %f seconds" % (end - start))
            print("memory = %d" % mem)
            print("cost = %d" % puzzle.cost)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:
            if p is None:
                continue
            mem += 1
            if tuple(p.array) not in visited:
                p.cost = puzzle.cost + misplacedTiles(p.array, final)
                pq.put((misplacedTiles(p.array, final),p))

    raise Exception("Puzzle cannot be solved")

def aStar_misplaced(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if solvability(root) != solvability(final):
        print("There is no path between the initial configuration and the final configuration.")
        return 0

    print("Initial Configuration:")
    board(root)
    print("Final Configuration:")
    board(final)
    inicial = Puzzle(root)
    pq = PriorityQueue()
    pq.put((misplacedTiles(root, final), inicial))            # adicionar a configuracao atual à fila, com a prioridade inicial
    visited = set()                                                    # criar uma lista com apenas as configuracoes visitadas
    mem = 0

    while not pq.empty():
        _, puzzle = pq.get()                                           # obter o próximo estado na fila

        if tuple(puzzle.array) in visited:                             # verificar se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:                                      # verificar se a configuração atual é igual à configuração final
            end = time.time()

            print("A* Misplaced: %d steps" % puzzle.depth)
            print("time = %f seconds" % (end - start))
            print("memory = %d" % mem)
            print("cost = %d" % puzzle.cost)            
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down, up, right, left]:
            if p is None:
                continue
            mem += 1
            if tuple(p.array) not in visited:
                priority = misplacedTiles(puzzle.array,p.array) + misplacedTiles(p.array, final)
                p.cost = puzzle.cost + priority
                pq.put((priority, p))

    raise Exception("Puzzle cannot be solved")


def aStar_manhattan(root: list[int], final: list[int]) -> Puzzle:
    start = time.time()

    if solvability(root) != solvability(final):
        print("There is no path between the initial configuration and the final configuration.")
        return 0

    print("Initial Configuration:")
    board(root)
    print("Final Configuration:")
    board(final)

    inicial = Puzzle(root)
    pq = PriorityQueue()
    pq.put((manhattanDistance(root, final), inicial))             # adicionar a configuracao atual à fila, com a prioridade inicial
    visited = set()                                                         # criar uma lista com apenas as configuracoes visitadas
    mem = 0
    

    while not pq.empty():
        _, puzzle = pq.get()                                                # obter o próximo estado na fila

        if tuple(puzzle.array) in visited:                                  # verificar se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:                                          # verificar se a configuração atual é igual à configuração final
            end = time.time()

            print("A* Manhattan: %d steps" % puzzle.depth)
            print("time = %f seconds" % (end - start))
            print("memory = %d" % mem)
            print("cost = %d" % puzzle.cost)
            return 0

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down, up, right, left]:
            if p is None:
                continue
            mem += 1
            if tuple(p.array) not in visited:
                priority = manhattanDistance(puzzle.array,p.array) + manhattanDistance(p.array, final)
                # manhattanDistance(puzzle.array,p.array) -> custo de sair da posicao anterior para a posicao atual
                # manhattanDistance(p.array, final) -> custo que falta para chegar ao final
                p.cost = puzzle.cost + priority
                pq.put((priority, p))

    raise Exception("Puzzle cannot be solved")
