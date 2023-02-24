from solvability import solvability
from functions import dfs, bfs, ids, g, a

def main():

    initial = list(map(int,input().split()))
    final = list(map(int,input().split()))

    if solvability(initial) == solvability(final):
        print("Depth-First-Search: ", dfs(initial,final))
        print("Breadth-First-Search: ", bfs(initial,final))
        print("Iterative-Deepening-Search: ", ids(initial,final))
        print("Greedy: ", g(initial,final))
        print("A*: ", a(initial,final))

    else:
        print("Não existe caminho entre a configuração final e a configuração inicial.")

main()
