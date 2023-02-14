

ar = []

for j in range(0, 10):
    anotherarray = []
    for i in range(0, 10):
        anotherarray.append(0)       
    ar.append(anotherarray)


    
locx = 1
locy = 3

ar[locy][locx] = 1

for x in ar:
    print(x)