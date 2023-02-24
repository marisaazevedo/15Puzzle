def solvability(a):

    line = 4
    inv = 0
    blankRow = 0

    for i in range (0,16):
        for j in range(i + 1, 16):
            if(a[j] < a[i] and a[j] != 0):
                inv += 1
        if(a[i] == 0):
            blankRow = line
        if((i + 1) % 4 == 0):
            line -= 1
    print ("inversoes:%d, blankrow:%d" %(inv,blankRow))
    return (inv % 2 == 0) == (blankRow % 2 == 1)

def main():

    initial = list(map(int,input().split()))
    final = list(map(int,input().split()))

    if solvability(initial) == solvability(final):
        print (True)
    else:
        print("Não existe caminho entre a configuração final e a configuração inicial.")

main()
