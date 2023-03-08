from auxFunctions import Puzzle
from collections import deque
from queue import PriorityQueue
import heapq
import sys

def misplacedTiles(puzzle, final):
    count = 0
    for i in range(16):
        if puzzle[i] != final[i]: # and puzzle[i] != 0
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

        if tuple(puzzle.array) in visited:  # verificar se configuracao atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:           # verificar se a configuração atual é igual à configuracao final
            print(len(nodes))
            return puzzle.depth             # retorna o números passos para chegar da configuracao inicial à final

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:
            if tuple(p) not in visited:
                stack.append(Puzzle(p, depth = puzzle.depth + 1))

    raise Exception("Puzzle cannot be solved")

def bfs(root: list[int], final: list[int]):
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
            print(mem)
            return puzzle.depth                 # retorna o números passos para chegar da configuracao inicial à final

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [left,right,up,down]:
            if tuple(p) not in visited:
                queue.append(Puzzle(p, depth = puzzle.depth + 1))
                mem += 1

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
                left = puzzle.left()
                right = puzzle.right()
                up = puzzle.up()
                down = puzzle.down()

                for p in [down,up,right,left]:
                    if tuple(p) not in visited:
                        stack.append(Puzzle(p, depth = puzzle.depth + 1))
        max_depth += 1
        if max_depth > sys.maxsize:                 # numero arbitrario para limitar a profundidade
            break

    raise Exception("Puzzle cannot be solved")

def greedy_manhattan(root: list[int], final: list[int]) -> Puzzle:
    visited = set()
    q = PriorityQueue()
    q.put(Puzzle(root), manhattanDistance(root, final))

    while not q.empty():
        puzzle = q.get()
        if puzzle.array == final:
            return puzzle.depth
        visited.add(tuple(puzzle.array))
        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:
            if tuple(p) not in visited:
                q.put(Puzzle(p, puzzle.depth + 1), (manhattanDistance(p, final)))

    raise Exception("Puzzle cannot be solved")

def greedy_misplaced(root: list[int], final: list[int]) -> Puzzle:
    h = misplacedTiles(root, final)  # calcula a heurística inicial, ou seja, o numero de pecas fora do lugar de acordo com a configuração final
    pq = PriorityQueue()                        # cria uma fila de prioridade vazia
    pq.put((h,Puzzle(root)))      # adiciona a configuração inicial à fila com a heurística calculada

    visited = set()                     # cria uma lista com apenas as configurações visitadas
    nodes = deque()                     # cria 

    while not pq.empty():
        _, puzzle = pq.get()   # extrai a configuração com menor heurística da fila
        nodes.append(puzzle)

        if tuple(puzzle.array) in visited:  # verifica se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:           # verifica se a configuração atual é igual à configuração final
            print(len(nodes))
            return puzzle.depth             # retorna o número de passos para chegar da configuração inicial à final
        
        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down,up,right,left]:     
            if tuple(p) not in visited:
                pq.put((misplacedTiles(p, final), Puzzle(p,depth=puzzle.depth +1)))

    raise Exception("Puzzle cannot be solved")

def aStar_misplaced(root: list[int], final: list[int]) -> Puzzle:
    pq = PriorityQueue()
    pq.put((0 + misplacedTiles(root, final), Puzzle(root)))  # adicionar a configuracao atual à fila, com a prioridade inicial
    visited = set()  # criar uma lista com apenas as configuracoes visitadas
    nodes = deque()

    while not pq.empty():
        _, puzzle = pq.get()  # obter o próximo estado na fila

        if tuple(puzzle.array) in visited:  # verificar se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:  # verificar se a configuração atual é igual à configuração final
            print(len(nodes))
            return puzzle.depth  # retorna o números passos para chegar da configuracao inicial à final

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down, up, right, left]:
            if tuple(p) not in visited:
                priority = puzzle.depth + 1 + misplacedTiles(p, final)
                pq.put((priority, Puzzle(p, depth=puzzle.depth + 1)))
                nodes.append(puzzle)

    raise Exception("Puzzle cannot be solved")
    

def aStar_manhattan(root: list[int], final: list[int]) -> Puzzle:
    pq = PriorityQueue()
    pq.put((0 + manhattanDistance(root, final), Puzzle(root)))  # adicionar a configuracao atual à fila, com a prioridade inicial
    visited = set()  # criar uma lista com apenas as configuracoes visitadas
    nodes = deque()

    while not pq.empty():
        _, puzzle = pq.get()  # obter o próximo estado na fila

        if tuple(puzzle.array) in visited:  # verificar se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:  # verificar se a configuração atual é igual à configuração final
            print(len(nodes))
            return puzzle.depth  # retorna o números passos para chegar da configuracao inicial à final

        left = puzzle.left()
        right = puzzle.right()
        up = puzzle.up()
        down = puzzle.down()

        for p in [down, up, right, left]:
            if tuple(p) not in visited:
                priority = puzzle.depth + 1 + manhattanDistance(p, final)
                pq.put((priority, Puzzle(p, depth=puzzle.depth + 1)))
                nodes.append(puzzle)

    raise Exception("Puzzle cannot be solved")

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