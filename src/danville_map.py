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

def down(new_coordinate,map):
    if map[y+1][x] == " ":
        map[y][x],map[y+1][x] = map[y+1][x],map[y][x]
        new_coordinate += 1
    else:
        print("unable to move because of an obstacle")
    return new_coordinate

def up(new_coordinate,map):
    if map[y-1][x] == " ":
        map[y][x],map[y-1][x] = map[y-1][x],map[y][x]
        new_coordinate -= 1
    else:
        print("unable to move because of an obstacle")
    return new_coordinate

def right(new_coordinate,map):
    if map[y][x+1] == " ":
        map[y][x],map[y][x+1] = map[y][x+1],map[y][x]
        new_coordinate += 1
    else:
        print("unable to move because of an obstacle")
    return new_coordinate

def left(new_coordinate,map):
    if map[y][x-1] == " ":
        map[y][x],map[y][x-1] = map[y][x-1],map[y][x]
        new_coordinate -= 1
    else:
        print("unable to move because of an obstacle")
    return new_coordinate

while True:
    for i in range(10):
        for j in range(10):
            print(map[i][j],end=" ")
        print()
    move = input("")
    if move == "d": 
        x = right(x,map)
    elif move == "a": 
        x =left(x,map)
    elif move == "w": 
        y = up(y,map)
    elif move == "s":
        y = down(y,map)
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
