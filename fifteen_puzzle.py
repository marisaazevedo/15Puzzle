from solvability import solvability
from functions import dfs, bfs, ids, g, a
from tabuleiro import puzzle
import time

def main():

    initial = list(map(int, input().split()))
    final = list(map(int, input().split()))
    method = int(input())

    if solvability(initial) == solvability(final):
        method = int(input())
        if(method) == "dfs":
            start = time.time()
            print("Depth-First-Search: %d passos" %dfs(initial, final))
            end = time.time()
            print("time = %f segundos" %(end - start))
            print("memory = ...")
        elif(method) == "bfs":
            # print("Breadth-First-Search: ", bfs(initial, final))
            print("não está implementado")
        elif(method) == "ids":
            # print("Iterative-Deepening-Search: ", ids(initial, final))
            print("não está implementado")
        elif(method) == "greedy":
            # print("Greedy: ", g(initial,final))
            print("não está implementado")
        elif(method) == "A*":
            # print("A*: ", a(initial,final))
            print("não está implementado")
    else:
        print("There is no path between the final configuration and the initial configuration.")

    # configurações dadas em formato de tabuleiro
    # print("Initial Configuration:")
    # print(puzzle(initial))
    # print("Final Configuration:")
    # print(puzzle(final))

main()
