map = [["*","*","*","*","*","*","*","*","*","*"],
        ["*","P"," "," "," "," "," "," "," ","*"],
        ["*"," "," "," "," "," "," ","S"," ","*"],
        ["*"," ","X"," "," "," "," "," "," ","*"],
        ["*"," ","X","X","X"," "," "," "," ","*"],
        ["*"," "," "," "," "," "," "," "," ","*"],
        ["*"," "," "," ","L"," "," "," "," ","*"],
        ["*"," "," "," "," "," "," ","A"," ","*"],
        ["*"," "," "," "," "," "," "," "," ","*"],
        ["*","*","*","*","*","*","*","*","*","*"]]

x = 1
y = 1

move = ""

def down(y,x,map):
    update = y
    if map[y+1][x] == " ":
        map[y][x],map[y+1][x] = map[y+1][x],map[y][x]
        update += 1
    else:
        print("unable to move because of an obstacle")
    return update

def up(y,x,map):
    update = y
    if map[y-1][x] == " ":
        map[y][x],map[y-1][x] = map[y-1][x],map[y][x]
        update -= 1
    else:
        print("unable to move because of an obstacle")
    return update

def right(y,x,map):
    update = x
    if map[y][x+1] == " ":
        map[y][x],map[y][x+1] = map[y][x+1],map[y][x]
        update += 1
    else:
        print("unable to move because of an obstacle")
    return update

def left(y,x,map):
    update = x
    if map[y][x-1] == " ":
        map[y][x],map[y][x-1] = map[y][x-1],map[y][x]
        update -= 1
    else:
        print("unable to move because of an obstacle")
    return update

while True:
    for i in range(10):
        for j in range(10):
            print(map[i][j],end=" ")
        print()
    move = input("")
    if move == "d": 
        x = right(y,x,map)
    elif move == "a": 
        x =left(y,x,map)
    elif move == "w": 
        y = up(y,x,map)
    elif move == "s":
        y = down(y,x,map)
    # elif move == "battle":
    #     if map[x][y+1] == "X" or map[x][y-1] == "X" or map[x+1][y] == "X" or map[x-1][y] == "X":
    #         battle()
    #     else:
    #         print("no bush nearby")
    # elif move == "laboratory":
    #     if map[x][y+1] == "L" or map[x][y-1] == "L" or map[x+1][y] == "L" or map[x-1][y] == "L":
    #         laboratory()
    #     else:
    #         print("no laboratory nearby")
    # elif move == "arena":
    #     if map[x][y+1] == "A" or map[x][y-1] == "A" or map[x+1][y] == "A" or map[x-1][y] == "A":
    #         arena()
    #     else:
    #         print("no arena nearby")
    # else:
    #     if map[x][y+1] == "S" or map[x][y-1] == "S" or map[x+1][y] == "S" or map[x-1][y] == "S":
    #         shop()
    #     else:
    #         print("no shop nearby")