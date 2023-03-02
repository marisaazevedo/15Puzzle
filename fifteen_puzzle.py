from solvability import solvability
from functions import dfs, bfs, idfs, greedy_manhattan, greedy_misplaced, aStar_manhattan, aStar_misplaced
from tabuleiro import puzzle
import time

def main():

    initial = list(map(int, input().split()))
    final = list(map(int, input().split()))

    if solvability(initial) == solvability(final):
        method = str(input())
        if(method) == "dfs":
            start = time.time()
            print("Depth First Search: %d passos" %dfs(initial, final))
            end = time.time()
            print("time = %f segundos" %(end - start))
            print("memory = ...")
        elif(method) == "bfs":
            start = time.time()
            print("Breadth First Search: ", bfs(initial, final))
            end = time.time()
            print("time = %f segundos" %(end - start))
            print("memory = ...")
        elif(method) == "idfs":
            # print("Iterative Deepening Depth First-Search: ", ids(initial, final))
            print("não está implementado")
        elif(method) == "greedy misplaced":
            # print("Greedy Misplaced: ", greedy_misplaced(initial,final))
            print("não está implementado")
        elif(method) == "greedy manhattan":
            # print("Greedy Manhattan: ", greedy_manhattan(initial,final))
            print("não está implementado")
        elif(method) == "A* misplaced":
            # print("A* Misplaced: ", aStar_misplaced(initial,final))
            print("não está implementado")
        elif(method) == "A* manhattan":
            # print("A* Manhattan: ", aStar_manhattan(initial,final))
            print("não está implementado")
    else:
        print("There is no path between the final configuration and the initial configuration.")

    # configurações dadas em formato de tabuleiro
    # print("Initial Configuration:")
    # print(puzzle(initial))
    # print("Final Configuration:")
    # print(puzzle(final))

main()
