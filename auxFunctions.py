import copy

class Puzzle:
    def __init__(self, array, depth = 0):
        self.array = array
        self.depth = depth
        self.blank = self.findBlankSpace()

    #def __lt__(self, other):
        #return self.h < other.h

    def findBlankSpace(self):
        i = 0
        while self.array[i] != 0:
            i += 1
        return i

    def left(self):
        move = copy.deepcopy(self.array)
        if self.blank % 4 != 0:
            move[self.blank] = move[self.blank - 1]
            move[self.blank - 1] = 0
        return move

    def right(self):
        move = copy.deepcopy(self.array)
        if self.blank % 4 != 3:
            move[self.blank] = move[self.blank + 1]
            move[self.blank + 1] = 0
        return move

    def up(self):
        move = copy.deepcopy(self.array)
        if self.blank > 3:
            move[self.blank] = move[self.blank - 4]
            move[self.blank - 4] = 0
        return move

    def down(self):
        move = copy.deepcopy(self.array)
        if self.blank < 12:
            move[self.blank] = move[self.blank + 4]
            move[self.blank + 4] = 0
        return move
