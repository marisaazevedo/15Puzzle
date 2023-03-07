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
'''
def greedy_misplaced(root: list[int], final: list[int]) -> Puzzle:
    visited = set()
    q = PriorityQueue() # heapq
    q.put(Puzzle(root), misplacedTiles(root, final)) # por default a fila de prioridade organiza as configurações de forma crescente de acordo com a quantidade de peças "fora do sítio"

    while not q.empty():
        current = q.get() # retira o elemento com maior prioridade da fila
        if current.array == final: # verifica se é igual à configuração final
            return current.depth # se sim retorna a profundidade da configuraçao
        visited.add(tuple(current.array)) # se não adiciona a configuração à lista de todas as configurações já visitadas

        if tuple(current.left())not in visited:
            q.put(current.left(), misplacedTiles(current.left(), final))
        if tuple(current.right())not in visited:
            q.put(current.right(), misplacedTiles(current.left(), final))
        if tuple(current.up())not in visited:
            q.put(current.up(), misplacedTiles(current.left(), final))
        if tuple(current.down())not in visited:
            q.put(current.down(), misplacedTiles(current.left(), final))

    raise Exception("Puzzle cannot be solved")


I apologize for the confusion in my previous response.
Upon further inspection, the error message you are seeing is due to the fact that the _put() method of the PriorityQueue class has been called with incorrect number of arguments.
This is because the _put() method is an internal method of the PriorityQueue class, which should not be called directly.

Instead, you should use the put() method of the PriorityQueue class to add items to the priority queue.
The put() method takes a single argument, which is the item to be added to the priority queue. You can set the priority of the item by passing a tuple with two elements, where the first element is the priority value and the second element is the item.
'''


'''
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


'''
def greedy_misplaced(root: list[int], final: list[int]) -> Puzzle:
    h = misplacedTiles(root, final)   # calcula a heurística inicial
    pq = PriorityQueue()                           # cria uma fila de prioridade vazia
    pq.put((h,Puzzle(root)))      # adiciona a configuração inicial à fila com a heurística calculada

    visited = set()                     # cria uma lista com apenas as configurações visitadas
    nodes = deque()

    while not pq.empty():
        estupida , puzzle = pq.get()   # extrai a configuração com menor heurística da fila
        nodes.append(puzzle)

        if tuple(puzzle.array) in visited:  # verifica se a configuração atual já foi visitada
            continue
        visited.add(tuple(puzzle.array))

        if puzzle.array == final:           # verifica se a configuração atual é igual à configuração final
            print(len(nodes))
            return puzzle.depth             # retorna o número de passos para chegar da configuração inicial à final

        if tuple(puzzle.left())not in visited:
            pq.put((misplacedTiles(puzzle.left(), final), Puzzle(puzzle.left())))
        if tuple(puzzle.right())not in visited:
            pq.put((misplacedTiles(puzzle.right(), final), Puzzle(puzzle.right())))
        if tuple(puzzle.up())not in visited:
            pq.put((misplacedTiles(puzzle.up(),final), Puzzle(puzzle.up())))
        if tuple(puzzle.down())not in visited:
            pq.put((misplacedTiles(puzzle.down(), final), Puzzle(puzzle.down())))

    raise Exception("Puzzle cannot be solved")


'''

        # gera as configurações filhas
        left_puzzle = Puzzle(puzzle.left(), depth = puzzle.depth + 1) 
        right_puzzle = Puzzle(puzzle.right(), depth = puzzle.depth + 1) 
        up_puzzle = Puzzle(puzzle.up(), depth = puzzle.depth + 1) 
        down_puzzle = Puzzle(puzzle.down(), depth = puzzle.depth + 1)
'''

'''
        # adiciona as configurações filhas com as heurísticas calculadas à fila de prioridade
        for p in [left_puzzle, right_puzzle, up_puzzle, down_puzzle]:
            if p and tuple(p.array) not in visited:
                h = misplacedTiles(p.array, final)  # calcula a heurística da configuração filha
                heapq.heappush(pq, (p, h))          # adiciona a configuração filha com a heurística à fila de prioridade
'''

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