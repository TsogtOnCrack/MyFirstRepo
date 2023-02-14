#loc format: [xcord, ycord]
loc = [2,2]
map = []

import sys
import tty

def draw(loc, map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if loc[0] == x and loc[1] == y:
                map[y][x] = 5
            else: map[y][x] = 0
    
    print()
    print()
    print()
    print()
    
    for line in map:
        print(line)
    

def setup():
    global map
    global loc
    #take in width and height inputs
    height = int(input("enter heigt:_ "))
    width = int(input("enter width:_ "))

    map = []

    #make the map
    for i in range(height):
        temp = []
        for j in range(width):
            temp.append(0)
        map.append(temp)
        
    draw(loc, map)


    
        
    

setup()

#just the thigns needed take key press input. Dont worry about it.
tty.setcbreak(sys.stdin)
key = ord(sys.stdin.read(1))

while True:
    
    if key == ord("c"):
        print("game end.")
        break
        
    if key == ord("a"):
        loc[0] -= 1
        draw(loc, map)
        
        
    if key == ord("s"):
        loc[1] += 1
        draw(loc, map)
    if key == ord("d"):
        loc[0] += 1
        draw(loc, map)
    if key == ord("w"):
        loc[1] -= 1
        draw(loc, map)

        
    key = ord(sys.stdin.read(1))
