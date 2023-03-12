from stratagies import dfs, bfs, idfs, greedy_misplaced, greedy_manhattan, aStar_misplaced, aStar_manhattan
import copy

class Puzzle:
    def __init__(self,array, depth = 0, parent = [], cost = 0):
        self.array = array
        self.parent = parent # array com os movimentos
        self.cost = cost
        self.depth = depth
        self.blank = self.findBlankSpace()

    def __lt__(self, other):
        return self.array < other.array

    def findBlankSpace(self):
        i = 0

        while self.array[i] != 0:
            i += 1

        return i

    def left(self):
        move = copy.deepcopy(self.array) # copia da configuração do pai
        backtrack = copy.deepcopy(self.parent) # copia dos movimentos do pai e depois é adicionado o movimento efetuado

        if self.blank % 4 != 0:
            move[self.blank] = move[self.blank - 1]
            move[self.blank - 1] = 0
            backtrack.append('Left')
        tab = Puzzle(move, depth = self.depth + 1, parent = backtrack)
        return tab

    def right(self):
        move = copy.deepcopy(self.array)
        backtrack = copy.deepcopy(self.parent)

        if self.blank % 4 != 3:
            move[self.blank] = move[self.blank + 1]
            move[self.blank + 1] = 0
            backtrack.append('Rigth')
        tab = Puzzle(move, depth = self.depth + 1, parent = backtrack)
        return tab

    def up(self):
        move = copy.deepcopy(self.array)
        backtrack = copy.deepcopy(self.parent)

        if self.blank > 3:
            move[self.blank] = move[self.blank - 4]
            move[self.blank - 4] = 0
            backtrack.append('Up')
        tab = Puzzle(move, depth = self.depth + 1, parent = backtrack)
        return tab

    def down(self):
        move = copy.deepcopy(self.array)
        backtrack = copy.deepcopy(self.parent)

        if self.blank < 12:
            move[self.blank] = move[self.blank + 4]
            move[self.blank + 4] = 0
            backtrack.append('Down')
        tab = Puzzle(move, depth = self.depth + 1, parent = backtrack)
        return tab
