def puzzle(t):
    tabuleiro = []
    for i in range(0,16,4):
        l = []
        for j in range(i,i+4):
            l.append(t[j])
        tabuleiro.append(l)
    return tabuleiro
