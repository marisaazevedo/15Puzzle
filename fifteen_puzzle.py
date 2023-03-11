from functions import dfs, bfs, idfs, greedy_misplaced,  aStar_manhattan, aStar_misplaced ,greedy_manhattan
import sys

def main():
    method = str(input())

    initial = list(map(int, input().split()))
    final = list(map(int, input().split()))

    if method == "DFS":
        dfs(initial,final)

    elif method == "BFS":
        bfs(initial, final)

    elif method == "IDFS":
        idfs(initial, final)

    elif method == "Greedy-Misplaced":
        greedy_misplaced(initial,final)

    elif method == "Greedy-Manhattan":
        greedy_manhattan(initial,final)

    elif method == "A-Star-Misplaced":
        aStar_misplaced(initial,final)

    elif method == "A-Star-Manhattan":
        aStar_manhattan(initial,final)

    else:
        print("No strategy found")

main()
    #sys.argv[1]
    # configurações dadas em formato de tabuleiro
    # print("Initial Configuration:")
    # print(puzzle(initial))
    # print("Final Configuration:")
    # print(puzzle(final))
