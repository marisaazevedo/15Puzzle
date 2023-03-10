def board(t):
    count = 1
    linha = "|"
    print(" ____ ____ ____ ____ ")

    for i in range(16):
        if t[i] <= 9:
            linha += " %d  |" %t[i]
        elif t[i >= 10]:
            linha += " %d |" %t[i]
        if count == 4:
            print(linha)
            print(" ____ ____ ____ ____ ")
            count = 0
            linha = "|"
        count += 1
    return ""
