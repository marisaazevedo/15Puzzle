import copy


class auxFunctions():

    def __init__(self, a, lastMove = None, depth = 0):
        self.a = a                  #array com a configuração do pai (anterior)
        self.findBlankSpace()
        self.lastMove = lastMove    #array de string que armazena os últimos movimentos feito pela configuração
        self.depth = depth
        self.child = []             #array para armazenar a nova configuração filha


    def findBlankSpace(self):
        i = 0
        while (self.a[i] != 0):
            i += 1
        return i

    def left(self,i):
        move = copy.deepcopy(self.a)
        lmove = copy.deepcopy(self.lasMove)
        if lmove is None:

        if( i % 4 != 0):
            move[i] = move[i -1]
            move[i - 1] = 0


[ ' up ', left, down, ri]


#        0  1  2  3
#
#    0   0  1  2  3
#    1   4  5  6  7
#    2   8  9  10 11
#    3   12 13 14 15


1  2  5  3
4  7  8  9
10 13 14 15
6  11 12 0

1  2  5  3
4  7  8  9
10 13 14 15
6  11 0  12

1  2  5  3
4  7  8  9
10 13 14 0
6  11 12 15
