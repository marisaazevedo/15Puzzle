from stratagies import dfs, bfs, idfs, greedy_misplaced, greedy_manhattan, aStar_manhattan, aStar_misplaced
import sys

def main(method):
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

main(sys.argv[1])
