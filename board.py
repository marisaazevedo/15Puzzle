def board(t):
    linha = "|"
    print(" ---- ---- ---- ---- ")

    for i in range(16):
        linha += " %2d |" % t[i]
        if i % 4 == 3:
            print(linha)
            print(" ---- ---- ---- ---- ")
            linha = "|"
