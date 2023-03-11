import copy

class Puzzle:
    def __init__(self,array, depth = 0, parent= None , cost= 0):
        self.array = array
        self.parent = parent
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

        move = copy.deepcopy(self.array)
        backtrack = copy.deepcopy(self.parent)

        if(backtrack is None ):
            backtrack = ['Left']
        else:
            backtrack.append('Left')

        if self.blank % 4 != 0:
            move[self.blank] = move[self.blank - 1]
            move[self.blank - 1] = 0
        tab = Puzzle(move,depth=self.depth +1, parent= backtrack)
        
        return tab

    def right(self):

        move = copy.deepcopy(self.array)
        backtrack = copy.deepcopy(self.parent)

        if(backtrack is None ):
            backtrack = ['Rigth']
        else:
            backtrack.append('Rigth')

        if self.blank % 4 != 3:
            move[self.blank] = move[self.blank + 1]
            move[self.blank + 1] = 0
        tab = Puzzle(move,depth=self.depth +1, parent= backtrack)

        return tab

    def up(self):

        move = copy.deepcopy(self.array)
        backtrack = copy.deepcopy(self.parent)

        if(backtrack is None ):
            backtrack = ['Up']
        else:
            backtrack.append('Up')

        if self.blank > 3:
            move[self.blank] = move[self.blank - 4]
            move[self.blank - 4] = 0
        tab = Puzzle(move,depth=self.depth +1, parent= backtrack)

        return tab

    def down(self):

        move = copy.deepcopy(self.array)
        backtrack = copy.deepcopy(self.parent)

        if(backtrack is None ):
            backtrack = ['Down']
        else:
            backtrack.append('Down')
        
        if self.blank < 12:
            move[self.blank] = move[self.blank + 4]
            move[self.blank + 4] = 0
        tab = Puzzle(move,depth=self.depth +1, parent= backtrack)

        return tab
