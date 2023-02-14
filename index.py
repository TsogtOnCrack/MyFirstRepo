import sys
import tty
tty.setcbreak(sys.stdin)
key = ord(sys.stdin.read(1))

ar =[[0,0,0],[0,0,0],[0,0,0]]

def make_map(ar, loc):
    for i in range(0, len(ar)):
        for j in range(0, len(ar[i])):
            if loc[1] == i and loc[0] == j:
                ar[i][j] = 1
            else:
                ar[i][j] = 0

loc = [1,1]

make_map(ar, loc)
for x in ar:
    print(x)



while True:
    
    if key == 97:
        print("you pressed a so its gonna stop maybe")
        break

    if key == 98:
        print("thats b")
        loc[0] += 1
        
    if key == 99:
        print("thats c")
    
    if key == 100:
        loc[0] -= 1
        print("thats d")
        
    key = ord(sys.stdin.read(1))
    
    make_map(ar, loc)
    for x in ar:
        print(x)
        
    
sys.exit(0)
