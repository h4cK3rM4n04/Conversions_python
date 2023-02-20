def octet(n) :#Code_by_Jaurès_Ratsimbazafiharivola
    sep,j,x = " ",8,len(n)
    if x%8 != 0:
        n = "0"*(8-x%8) + n 
    L = [(n[i:i+j]) for i in range(0, len(n), j)]
    return sep.join(L)
print(octet("0101"))