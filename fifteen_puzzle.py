from functions import dfs, bfs, idfs, greedy_misplaced,  aStar_manhattan, aStar_misplaced ,greedy_manhattan
from tabuleiro import puzzle
import time

def main():

    initial = list(map(int, input().split()))
    final = list(map(int, input().split()))
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
        start = time.time()
        print("Iterative Deepening Depth First Search: ", idfs(initial, final))
        end = time.time()
        print("time = %f segundos" %(end - start))
        print("memory = ...")

    elif(method) == "greedy misplaced":
        start = time.time()
        print("Greedy Misplaced: ", greedy_misplaced(initial,final))
        end = time.time()
        print("time = %f segundos" %(end - start))

    elif(method) == "greedy manhattan":
        start = time.time()
        print("Greedy Manhattan: ", greedy_manhattan(initial,final))
        end = time.time()
        print("time = %f segundos" %(end - start))

    elif(method) == "A* misplaced":
        start = time.time()
        print("A* Misplaced: ", aStar_misplaced(initial,final))
        end = time.time()
        print("time = %f segundos" %(end - start))

    elif(method) == "A* manhattan":
        start = time.time()
        print("A* Manhattan: ", aStar_manhattan(initial,final))
        end = time.time()
        print("time = %f segundos" %(end - start))

    else:
        print("There is no path between the final configuration and the initial configuration.")

main()

    # configurações dadas em formato de tabuleiro
    # print("Initial Configuration:")
    # print(puzzle(initial))
    # print("Final Configuration:")
    # print(puzzle(final))
